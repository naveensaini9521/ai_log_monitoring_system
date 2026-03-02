from flask import Blueprint, request, jsonify
from services.log_service import LogService

ingest_bp = Blueprint("ingest", __name__)

@ingest_bp.route("/ingest", methods=["POST"])
def ingest_log():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON payload provided"}), 400

        log_id = LogService.create_log(data)

        return jsonify({"id": log_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500