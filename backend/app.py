from flask import Flask
from config import Config
from extensions import db, cors, jwt

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
cors.init_app(app)
jwt.init_app(app)

# Import blueprints after app and extensions are ready to avoid circular imports
from auth import auth_bp

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")

# Auto-create tables on startup
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)