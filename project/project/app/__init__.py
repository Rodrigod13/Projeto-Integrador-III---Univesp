from flask import Flask
from .infrastructure.database.db_config import DatabaseConfig, db
from .routes import register_routes

app = Flask(__name__)

db_config = DatabaseConfig(app)

with app.app_context():
    db_config.create_tables()

register_routes(app)
