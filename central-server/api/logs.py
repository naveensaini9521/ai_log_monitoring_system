from flask import Blueprint, request, jsonify
from services.log_service import get_logs

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/logs", methods=["GET"])
def fetch_logs():
    try:
        filters = {}

        level = request.args.get("level")
        service = request.args.get("service")
        source = request.args.get("source")

        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 20))

        if level:
            filters["level"] = level
        if service:
            filters["service"] = service
        if source:
            filters["source"] = source

        result = get_logs(filters, page, limit)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500