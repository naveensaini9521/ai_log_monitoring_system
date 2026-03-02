import os
from flask import Flask
from config import DevelopmentConfig
from extensions import mongo, cors
from api.ingest import ingest_bp
from api.health import health_bp
from api.logs import logs_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Init extensions
    mongo.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(ingest_bp, url_prefix="/api")
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(logs_bp, url_prefix="/api")
    
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=5000)