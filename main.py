from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "GradeMyLC is live 🚀"

@app.route("/grade", methods=["POST"])
def grade():
    data = request.get_json()
    return jsonify({
        "message": "Backend working",
        "received": data
    })

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
