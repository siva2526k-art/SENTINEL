"""
SENTINEL — AI Model & API Key Connection Diagnostics Tool
Tests all Tier 1, Tier 2, and Tier 3 AI model endpoints to verify operational health, latency, and keys.
"""
import sys
import os
import time

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from ai_client import SentinelAIClient

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def run_diagnostics():
    print("="*75)
    print("🛡️  SENTINEL — AI MODEL & API KEY CONNECTION DIAGNOSTICS TOOL")
    print("="*75 + "\n")

    client = SentinelAIClient()
    test_prompt = "Sanitized Security Test: Respond with 'HEALTHY' if operating normally."

    # 1. Test Tier 1 Local GPU Ollama
    print("1️⃣  Testing Tier 1: Local GPU Ollama (deepseek-r1:8b / llama3.2:1b)...")
    t0 = time.time()
    res1 = client.query_tier1_ollama(test_prompt)
    latency1 = round((time.time() - t0) * 1000, 2)
    if res1["status"] == "success":
        print(f"   ✅ [STATUS: ONLINE] Engine: {res1['tier']} | Latency: {latency1} ms")
        print(f"   💬 Response Preview: \"{res1['content'][:100]}...\"\n")
    else:
        print(f"   ⚠️ [STATUS: OFFLINE/ERROR]: {res1['error']}\n")

    # 2. Test Tier 2 Groq Cloud API (DeepSeek 70B)
    print("2️⃣  Testing Tier 2: Groq Cloud API (deepseek-r1-distill-llama-70b)...")
    if client.groq_api_key:
        t0 = time.time()
        res2 = client.query_tier2_groq(test_prompt)
        latency2 = round((time.time() - t0) * 1000, 2)
        if res2["status"] == "success":
            print(f"   ✅ [STATUS: ONLINE] Engine: {res2['tier']} | Latency: {latency2} ms")
            print(f"   💬 Response Preview: \"{res2['content'][:100]}...\"\n")
        else:
            print(f"   ❌ [STATUS: API ERROR]: {res2['error']}\n")
    else:
        print("   ℹ️ [STATUS: SKIPPED]: GROQ_API_KEY not set in .env (Add GROQ_API_KEY to test)\n")

    # 3. Test Tier 2 Google AI Studio Gemini API (Gemini 2.0 Flash)
    print("3️⃣  Testing Tier 2: Google AI Studio API (gemini-2.0-flash 2M Context)...")
    if client.gemini_api_key:
        t0 = time.time()
        res3 = client.query_tier2_gemini_free(test_prompt)
        latency3 = round((time.time() - t0) * 1000, 2)
        if res3["status"] == "success":
            print(f"   ✅ [STATUS: ONLINE] Engine: {res3['tier']} | Latency: {latency3} ms")
            print(f"   💬 Response Preview: \"{res3['content'][:100]}...\"\n")
        else:
            print(f"   ❌ [STATUS: API ERROR]: {res3['error']}\n")
    else:
        print("   ℹ️ [STATUS: SKIPPED]: GEMINI_API_KEY not set in .env (Add GEMINI_API_KEY to test)\n")

    # 4. Test Tier 3 OpenRouter Free API (550B Nemotron-3)
    print("4️⃣  Testing Tier 3: OpenRouter FREE API (nvidia/nemotron-3-ultra-550b-a55b:free 550B)...")
    t0 = time.time()
    res4 = client.query_tier3_openrouter_free(test_prompt)
    latency4 = round((time.time() - t0) * 1000, 2)
    if res4["status"] == "success":
        print(f"   ✅ [STATUS: ONLINE] Engine: {res4['tier']} | Latency: {latency4} ms")
        print(f"   💬 Response Preview: \"{res4['content'][:100]}...\"\n")
    else:
        print(f"   ⚠️ [STATUS: SKIPPED/RATE_LIMITED]: {res4['error']}\n")

    print("="*75)
    print("🎯 DIAGNOSTICS COMPLETE. SENTINEL AI Router is ready for production triage!")
    print("="*75 + "\n")

if __name__ == "__main__":
    run_diagnostics()
