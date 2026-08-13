"""
SENTINEL — Live Wazuh SIEM Telemetry Webhook Listener
Listens for incoming HTTP POST JSON alert webhooks from Wazuh SIEM / Syslog managers and pipes them into SENTINEL.
"""
import sys
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from triage_agent import SentinelTriageAgent

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

agent_instance = SentinelTriageAgent()

class WazuhWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            raw_log = payload.get("raw_alert") or payload.get("full_log") or json.dumps(payload)
            
            print(f"\n📥 [WAZUH WEBHOOK RECEIVED]: Ingesting live syslog payload...")
            result = agent_instance.process_alert(raw_log)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response_data = {"status": "SUCCESS", "incident_id": "INC-2026-8801", "triage_verdict": result["triage"]["severity"]}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ERROR", "error": str(e)}).encode('utf-8'))

    def log_message(self, format, *args):
        # Silence default HTTP server access logs
        return

class SentinelWazuhListener:
    def __init__(self, host="0.0.0.0", port=9000):
        self.host = host
        self.port = port

    def start_listener(self):
        server_address = (self.host, self.port)
        httpd = HTTPServer(server_address, WazuhWebhookHandler)
        print(f"📡 [SENTINEL WAZUH LISTENER]: Active & listening for SIEM webhooks at http://{self.host}:{self.port}/api/v1/wazuh")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Webhook listener stopped.")

if __name__ == "__main__":
    listener = SentinelWazuhListener(port=9000)
    print("📡 Initializing Wazuh Webhook Listener on port 9000...")
