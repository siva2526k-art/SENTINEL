"""
SENTINEL — Persistent ChromaDB Vector RAG Threat Memory Store (Phase 2)
Stores sanitized security incidents, MITRE metadata, and analyst resolutions.
Retrieves top-k historical threat patterns to inform AI triage without exposing raw PII.
STRICT PRIVACY ISOLATION: NEVER stores raw PII or identity_map in vector embeddings or metadata.
"""
import os
import sys
import json
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import chromadb
    from chromadb.config import Settings
    HAS_CHROMADB = True
except ImportError:
    HAS_CHROMADB = False

class SentinelMemoryStore:
    def __init__(self, chroma_db_dir=r"C:\Users\siva2\Projects\SENTINEL\data\chroma"):
        self.chroma_db_dir = chroma_db_dir
        os.makedirs(self.chroma_db_dir, exist_ok=True)
        
        self.use_real_chroma = HAS_CHROMADB
        if self.use_real_chroma:
            try:
                self.client = chromadb.PersistentClient(path=self.chroma_db_dir)
                self.collection = self.client.get_or_create_collection(
                    name="sentinel_threat_memory",
                    metadata={"description": "Sanitized historical security incidents for SENTINEL AI RAG"}
                )
            except Exception as e:
                print(f"⚠️ ChromaDB Init Warning: {e}. Falling back to In-Memory RAG Store.")
                self.use_real_chroma = False
                self.in_memory_store = {}
        else:
            self.in_memory_store = {}

    def _sanitize_metadata(self, metadata: dict) -> dict:
        """Ensure no raw PII, identity_map, or complex objects exist in metadata."""
        safe_meta = {}
        if not metadata:
            return safe_meta

        for k, v in metadata.items():
            if k in ["identity_map", "ip_map", "raw_alert"]:
                continue
            if isinstance(v, (str, int, float, bool)):
                safe_meta[k] = v
            else:
                safe_meta[k] = str(v)
        return safe_meta

    def add_incident(self, incident_id: str, sanitized_text: str, metadata: dict = None) -> bool:
        """
        Insert sanitized incident into ChromaDB vector store.
        """
        if not incident_id or not sanitized_text:
            return False

        safe_metadata = self._sanitize_metadata(metadata)
        safe_metadata["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        if self.use_real_chroma:
            try:
                self.collection.upsert(
                    documents=[sanitized_text],
                    metadatas=[safe_metadata],
                    ids=[incident_id]
                )
                return True
            except Exception as e:
                print(f"⚠️ ChromaDB Upsert Exception: {e}")
                return False
        else:
            self.in_memory_store[incident_id] = {
                "document": sanitized_text,
                "metadata": safe_metadata
            }
            return True

    def search_similar_incidents(self, sanitized_text: str, top_k: int = 3) -> list:
        """
        Query ChromaDB vector store for top-k similar historical threat patterns.
        """
        if not sanitized_text:
            return []

        if self.use_real_chroma:
            try:
                results = self.collection.query(
                    query_texts=[sanitized_text],
                    n_results=top_k
                )
                
                similar_incidents = []
                if results and "documents" in results and results["documents"]:
                    docs = results["documents"][0]
                    metas = results["metadatas"][0] if "metadatas" in results else [{}]*len(docs)
                    ids = results["ids"][0] if "ids" in results else ["INC-UNK"]*len(docs)

                    for i in range(len(docs)):
                        similar_incidents.append({
                            "incident_id": ids[i],
                            "sanitized_summary": docs[i],
                            "metadata": metas[i]
                        })
                return similar_incidents
            except Exception as e:
                print(f"⚠️ ChromaDB Query Exception: {e}")
                return []
        else:
            # Fallback simple keyword match
            matches = []
            words = set(sanitized_text.lower().split())
            for inc_id, data in self.in_memory_store.items():
                doc_words = set(data["document"].lower().split())
                overlap = len(words.intersection(doc_words))
                if overlap > 0:
                    matches.append({
                        "incident_id": inc_id,
                        "sanitized_summary": data["document"],
                        "metadata": data["metadata"],
                        "score": overlap
                    })
            sorted_matches = sorted(matches, key=lambda x: x.get("score", 0), reverse=True)
            return sorted_matches[:top_k]

    def update_resolution(self, incident_id: str, analyst_resolution: str) -> bool:
        """Update historical analyst resolution for an incident."""
        if self.use_real_chroma:
            try:
                existing = self.collection.get(ids=[incident_id])
                if existing and existing.get("metadatas") and existing["metadatas"][0]:
                    meta = existing["metadatas"][0]
                    meta["analyst_resolution"] = analyst_resolution
                    doc = existing["documents"][0]
                    self.collection.upsert(documents=[doc], metadatas=[meta], ids=[incident_id])
                    return True
            except Exception as e:
                print(f"⚠️ ChromaDB Resolution Update Exception: {e}")
                return False
        else:
            if incident_id in self.in_memory_store:
                self.in_memory_store[incident_id]["metadata"]["analyst_resolution"] = analyst_resolution
                return True
        return False

if __name__ == "__main__":
    memory = SentinelMemoryStore()

    print("🧠 Testing ChromaDB Persistent RAG Memory Store...")
    memory.add_incident(
        incident_id="INC-2026-001",
        sanitized_text="Failed SSH authentication for user [USER_1] from [INTERNAL_IP_1] on port 22. 500 failed attempts.",
        metadata={"mitre": "T1110", "severity": "HIGH", "source": "wazuh"}
    )
    
    memory.add_incident(
        incident_id="INC-2026-002",
        sanitized_text="Process Creation: powershell.exe -EncodedCommand on host POLICE-HQ-PC04 user [USER_1].",
        metadata={"mitre": "T1059", "severity": "HIGH", "source": "sysmon"}
    )

    results = memory.search_similar_incidents("Failed SSH login attempt from internal IP on port 22", top_k=2)
    print(f"\n🔍 Search Results (Top 2 Similar Threats):")
    print(json.dumps(results, indent=2))
