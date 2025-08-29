from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

ALLOWED_ALERTS = {"NginxDown", "HighHostCPU"}

@app.route("/", methods=["GET"])
def index():
    return "Healer webhook up", 200

@app.route("/alert", methods=["POST"])
def alert():
    data = request.get_json(force=True, silent=True) or {}
    alerts = [a for a in data.get("alerts", []) if a.get("labels", {}).get("alertname") in ALLOWED_ALERTS]

    if not alerts:
        return jsonify({"status": "ignored"}), 200

    try:
        # Run ansible playbook (local docker control via /var/run/docker.sock)
        cmd = ["ansible-playbook", "-i", "ansible/inventory.ini", "ansible/heal.yml", "-v"]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return jsonify({"status": "ok", "stdout": result.stdout[-2000:]}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "stdout": e.stdout[-2000:], "stderr": e.stderr[-2000:]}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
