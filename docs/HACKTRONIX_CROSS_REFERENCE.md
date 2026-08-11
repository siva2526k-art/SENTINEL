# ⚡ HackTronix 2.0 & SENTINEL — Cross-Project Knowledge Bridge

> **Purpose**: Connects technical specifications, shared local AI runtimes, vision telemetry, and agent state architectures between **HackTronix 2.0** and **SENTINEL**.

---

## 📌 Project Overview & Shared Infrastructure

| Attribute | SENTINEL Project | HackTronix 2.0 Projects |
| :--- | :--- | :--- |
| **Domain** | Cybersecurity & AI SOC Analyst | Computer Vision (Track B Task 1 & 2) + World Modeling Agent (Track B Theme 2) |
| **Workspace Location** | `C:\Users\siva2\Projects\SENTINEL` | `C:\Users\siva2\OneDrive\Desktop\hackatronix-monorepo`<br>`C:\Users\siva2\OneDrive\Desktop\Scripts\hacktronix_agent` |
| **Local AI Hardware** | NVIDIA RTX 3050 (6GB VRAM, CUDA 13.0) | NVIDIA RTX 3050 (6GB VRAM, CUDA 13.0) |
| **Local LLM Engine** | Ollama (`llama3.1:8b`, `deepseek-r1:8b`) | Ollama (`gemma2:2b`, `deepseek-r1:8b`) |
| **Live Web Demos** | In Development (FastAPI + React Dashboard) | • [BallVision AI Live Demo](https://hackatronix2-0.vercel.app/)<br>• [Face AI Telemetry Demo](https://hackatronix2-0-nl62.vercel.app/) |

---

## 🎯 HackTronix 2.0 Subsystems

### 1. ⚽ BallVision AI (Track B Task 1)
* **Goal**: Real-time monocular 2D/3D ball detection, velocity tracking, and trajectory prediction.
* **Tech Stack**: React, TypeScript, OpenCV.js, WebGL.
* **Location**: `C:\Users\siva2\OneDrive\Desktop\hackatronix-monorepo\ball-detection`

### 2. 👤 Monocular Face Distance Telemetry (Track B Task 2)
* **Goal**: Monocular face detection, depth estimation, and horizontal deviation angle estimation.
* **Tech Stack**: MediaPipe / FaceMesh, WebGPU / WebGL, React.
* **Location**: `C:\Users\siva2\OneDrive\Desktop\hackatronix-monorepo\face-detection`

### 3. 🤖 AI World Modeling Agent (Track B Theme 2)
* **Goal**: Bounded key-value memory store with local Ollama LLM (`gemma2:2b`) exploring cybersecurity text-adventure environments without continuous context accumulation.
* **Tech Stack**: Python, Ollama API, Bounded Cache Memory.
* **Location**: `C:\Users\siva2\OneDrive\Desktop\Scripts\hacktronix_agent`

---

## 🔗 Synergies & Integration Points with SENTINEL

1. **Shared Ollama Local LLM Infrastructure**:
   * Both projects share the same local RTX 3050 GPU and Ollama server instance.
   * `hacktronix_agent` uses local `gemma2:2b` / `deepseek-r1:8b` for extraction & belief checking; SENTINEL uses `llama3.1:8b` / `deepseek-r1:8b` for Zero-Trust alert triage.

2. **Bounded Memory & RAG Parallel**:
   * `hacktronix_agent`'s `world_model.py` (key-value RAM/SSD caching) mirrors SENTINEL's `src/memory.py` (ChromaDB RAG vector store for historical threat memory).

3. **Multi-Agent Coordination**:
   * HackTronix vision & world-model agents feed environmental state to the local LLM, similar to how SENTINEL's Zero-Trust Sanitizer feeds sanitized log events to the 3-Tier AI Router.
