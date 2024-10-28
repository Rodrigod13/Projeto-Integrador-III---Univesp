from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatabaseConfig:
    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(app)

    def create_tables(self):
        with db.engine.connect() as connection:
            db.create_all()
