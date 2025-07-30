import os
import sys
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

from user import db, User  # Local SQLAlchemy model
from ml_model import PredictiveMaintenanceModel

# Detect project root dynamically and ensure it is in the import path
PROJECT_ROOT = os.path.dirname(__file__)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --------------------------------------------------------------------------------------
# App & Config
# --------------------------------------------------------------------------------------
app = Flask(__name__, static_folder=os.path.join(PROJECT_ROOT, "static"))
app.config.update(
    SECRET_KEY="asdf#FGSgvasgf$5$WGT",
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(PROJECT_ROOT, 'app.db')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Enable CORS for ALL domains (adjust to your needs in production)
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

# --------------------------------------------------------------------------------------
# ML Model – load (or train & save) once on startup
# --------------------------------------------------------------------------------------
model_path = os.path.join(PROJECT_ROOT, "trained_model.pkl")
ml_model = PredictiveMaintenanceModel()
ml_model.load_model(model_path)

# --------------------------------------------------------------------------------------
# Helper utilities
# --------------------------------------------------------------------------------------

def _user_to_dict(user: User):
    """Serialize a User SQLAlchemy instance to a dict."""
    return {"id": user.id, "username": user.username, "email": user.email}

# --------------------------------------------------------------------------------------
# API ROUTES
# --------------------------------------------------------------------------------------

@app.route("/api/users", methods=["GET", "POST"])
def users():
    """GET ➡ list users · POST ➡ create user"""
    if request.method == "GET":
        return jsonify({"success": True, "data": [_user_to_dict(u) for u in User.query.all()]})

    # POST – create new user
    data = request.get_json(force=True)
    username = data.get("username")
    email = data.get("email")
    if not username or not email:
        return jsonify({"success": False, "error": "username and email are required"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"success": False, "error": "User already exists"}), 409

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "data": _user_to_dict(new_user)}), 201


@app.route("/api/predict", methods=["POST"])
def predict():
    """Return failure probability, status and alert level for posted sensor data."""
    data = request.get_json(force=True)

    try:
        temperature = float(data["temperature"])
        vibration = float(data["vibration"])
        pressure = float(data["pressure"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"success": False, "error": "temperature, vibration and pressure must be provided as numbers"}), 400

    try:
        failure_prob = ml_model.predict_failure_probability(temperature, vibration, pressure)
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 500

    status = ml_model.get_machine_status(failure_prob)
    alert_level = ml_model.get_alert_level(failure_prob)

    return jsonify(
        {
            "success": True,
            "data": {
                "failure_probability": failure_prob,
                "machine_status": status,
                "alert_level": alert_level,
            },
        }
    )

# --------------------------------------------------------------------------------------
# Static file serving (built React/Vite frontend)
# --------------------------------------------------------------------------------------

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react_app(path):
    """Serve React build files from the static folder (fallback to index.html)."""
    static_folder = app.static_folder
    if static_folder is None:
        return "Static folder not configured", 404

    requested_path = os.path.join(static_folder, path)
    if path and os.path.exists(requested_path):
        return send_from_directory(static_folder, path)

    # Fallback to index.html for client-side routing
    index_path = os.path.join(static_folder, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(static_folder, "index.html")

    return "index.html not found", 404

# --------------------------------------------------------------------------------------
# Local development entry point
# --------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Use PORT env var (e.g., Render, Railway) or default 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
