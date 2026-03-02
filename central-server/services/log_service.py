from datetime import datetime
from extensions import mongo
from services.validator import validate_log_payload


def get_logs(filters: dict, page: int = 1, limit: int = 20):

    skip = (page - 1) * limit

    cursor = (
        mongo.db.logs
        .find(filters)
        .sort("timestamp", -1)
        .skip(skip)
        .limit(limit)
    )

    logs = list(cursor)

    for log in logs:
        log["_id"] = str(log["_id"])

    total = mongo.db.logs.count_documents(filters)

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": logs
    }