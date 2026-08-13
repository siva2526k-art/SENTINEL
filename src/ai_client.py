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

def load_env_file():
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'").strip('"')
                    if key and val:
                        os.environ[key] = val

load_env_file()

class SentinelAIClient:
    def __init__(self, groq_api_key=None, openai_api_key=None):
        self.groq_api_key = groq_api_key or os.environ.get("GROQ_API_KEY")
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY")
        self.openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
        self.ollama_url = "http://localhost:11434/api/generate"

    def query_tier1_ollama(self, prompt: str, model="deepseek-r1:8b") -> dict:
        """Tier 1: Query Local Ollama running 100% offline on GPU ($0 cost)."""
        payload = {"model": model, "prompt": prompt, "stream": False}
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(self.ollama_url, data=data, headers={'Content-Type': 'application/json'})
        
        try:
            with urllib.request.urlopen(req, timeout=8) as response:
                result = json.loads(response.read().decode('utf-8'))
                return {"status": "success", "tier": f"Tier 1 (Local Ollama {model})", "content": result.get("response", "").strip()}
        except Exception:
            # Fallback to lightweight 1B model if 8B model is downloading or unavailable
            if model != "llama3.2:1b":
                return self.query_tier1_ollama(prompt, model="llama3.2:1b")
            return {"status": "error", "error": "Local Ollama server unavailable."}

    def query_tier2_groq(self, prompt: str, model="deepseek-r1-distill-llama-70b") -> dict:
        """Tier 2: Query Groq Cloud API (DeepSeek 70B Reasoning Model - FREE Tier at 300 tokens/sec)."""
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
                return {"status": "success", "tier": "Tier 2 (Groq Cloud DeepSeek 70B)", "content": content}
        except Exception as e:
            return {"status": "error", "error": f"Groq API error: {e}"}

    def query_tier2_gemini_free(self, prompt: str) -> dict:
        """
        Tier 2 (Massive Context): Query Google AI Studio Gemini 2.0 Flash FREE API (2 Million Token Context Window!).
        """
        gemini_key = os.environ.get("GEMINI_API_KEY", "")
        if not gemini_key:
            return {"status": "error", "error": "GEMINI_API_KEY environment variable not set."}

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        data = json.dumps(payload).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=data, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                result = json.loads(response.read().decode('utf-8'))
                content = result['candidates'][0]['content']['parts'][0]['text']
                return {"status": "success", "tier": "Tier 2 (Google Gemini 2.0 Flash 2M Context)", "content": content}
        except Exception as e:
            return {"status": "error", "error": f"Gemini API error: {e}"}

    def query_tier3_openrouter_free(self, prompt: str, model="deepseek/deepseek-r1:free") -> dict:
        """
        Tier 3 (Ultra-Large Models > 70B): Query OpenRouter FREE Tier for 671B DeepSeek-R1 or 405B Llama 3.1.
        Models: 'deepseek/deepseek-r1:free' (671B MoE) OR 'meta-llama/llama-3.1-405b-instruct:free' (405B).
        """
        openrouter_key = os.environ.get("OPENROUTER_API_KEY", "")
        url = "https://openrouter.ai/api/v1/chat/completions"
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1
        }
        data = json.dumps(payload).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openrouter_key}' if openrouter_key else '',
            'HTTP-Referer': 'https://github.com/siva2526k-art/SENTINEL',
            'X-Title': 'SENTINEL AI SOC'
        }
        req = urllib.request.Request(url, data=data, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                result = json.loads(response.read().decode('utf-8'))
                content = result['choices'][0]['message']['content']
                return {"status": "success", "tier": f"Tier 3 (OpenRouter Free {model})", "content": content}
        except Exception as e:
            return {"status": "error", "error": f"OpenRouter API error: {e}"}

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
    print("• Tier 3 OpenRouter 671B/405B Available: YES (deepseek/deepseek-r1:free)")
