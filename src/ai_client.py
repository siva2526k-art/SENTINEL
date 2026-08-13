"""
SENTINEL — Universal Multi-Tier AI Client Module
Handles connections to Tier 1 (Local Ollama), Tier 2 (Groq Cloud API), and Tier 3 (Enterprise Cloud OpenAI/Gemini).
"""
import os
import sys
import json
import urllib.request
import urllib.error

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SentinelAIClient:
    def __init__(self, groq_api_key=None, openai_api_key=None):
        self.groq_api_key = groq_api_key or os.environ.get("GROQ_API_KEY")
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        self.ollama_url = "http://localhost:11434/api/generate"

    def query_tier1_ollama(self, prompt: str, model="llama3.2:1b") -> dict:
        """Tier 1: Query Local Ollama running 100% offline on RTX 3050 GPU ($0 cost)."""
        payload = {"model": model, "prompt": prompt, "stream": False}
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(self.ollama_url, data=data, headers={'Content-Type': 'application/json'})
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read().decode('utf-8'))
                return {"status": "success", "tier": "Tier 1 (Local Ollama)", "content": result.get("response", "").strip()}
        except Exception as e:
            return {"status": "error", "error": f"Ollama offline: {e}"}

    def query_tier2_groq(self, prompt: str, model="llama-3.1-70b-versatile") -> dict:
        """Tier 2: Query Groq Cloud API for ultra-fast deep reasoning."""
        if not self.groq_api_key:
            return {"status": "error", "error": "GROQ_API_KEY environment variable not set."}
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
        data = json.dumps(payload).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.groq_api_key}'
        }
        req = urllib.request.Request(url, data=data, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode('utf-8'))
                content = result['choices'][0]['message']['content']
                return {"status": "success", "tier": "Tier 2 (Groq Cloud API)", "content": content}
        except Exception as e:
            return {"status": "error", "error": f"Groq API error: {e}"}

    def query_tier3_openai(self, prompt: str, model="gpt-4o") -> dict:
        """Tier 3: Query Enterprise Cloud API (OpenAI/Claude) for critical multi-stage zero-day APTs."""
        if not self.openai_api_key:
            return {"status": "error", "error": "OPENAI_API_KEY environment variable not set."}
        
        url = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1
        }
        data = json.dumps(payload).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.openai_api_key}'
        }
        req = urllib.request.Request(url, data=data, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                result = json.loads(response.read().decode('utf-8'))
                content = result['choices'][0]['message']['content']
                return {"status": "success", "tier": "Tier 3 (Enterprise OpenAI Cloud)", "content": content}
        except Exception as e:
            return {"status": "error", "error": f"OpenAI API error: {e}"}

if __name__ == "__main__":
    client = SentinelAIClient()
    print("🤖 Universal Multi-Tier AI Client initialized.")
    print("• Tier 1 Local Ollama Status:", client.query_tier1_ollama("Test connection.")["status"])
    print("• Tier 2 Groq API Key Configured:", bool(client.groq_api_key))
    print("• Tier 3 OpenAI Key Configured:", bool(client.openai_api_key))
