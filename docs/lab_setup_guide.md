# 🧪 SENTINEL Lab Setup Guide

## 📋 Weekend Lab Configuration Plan

### Step 1: Install VirtualBox
1. Download Oracle VM VirtualBox for Windows from [virtualbox.org](https://www.virtualbox.org).
2. Install with default settings.

### Step 2: Set Up Kali Linux VM
1. Download pre-built Kali Linux VirtualBox image from [kali.org/get-kali](https://www.kali.org/get-kali/).
2. Import `.vbox` image into VirtualBox.
3. Allocate 4 GB RAM + 2 CPU cores.

### Step 3: Set Up Local Ollama Engine
1. Download Ollama for Windows from [ollama.com](https://ollama.com).
2. Open PowerShell and pull the local 8B model:
   ```powershell
   ollama pull llama3.1:8b
   # Or for fast reasoning:
   ollama pull deepseek-r1:8b
   ```
3. Test local execution on RTX 3050:
   ```powershell
   ollama run llama3.1:8b "Summarize this alert: SSH brute force from IP 192.168.1.100"
   ```

### Step 4: Set Up Wazuh SIEM Lab (Semester 4 Prep)
1. Download Wazuh All-in-One Virtual Machine from [wazuh.com](https://wazuh.com).
2. Import into VirtualBox on Host-Only Network.
3. Access Wazuh Dashboard at `https://localhost:8443`.
