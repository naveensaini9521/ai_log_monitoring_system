# central-server/models/log_model.py

from datetime import datetime
from app.extensions import db

class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow   # 🔥 FIX
    )

    level = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)

    source = db.Column(db.String(50), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)

    raw_log = db.Column(db.JSON, nullable=False)