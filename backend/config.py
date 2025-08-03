import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "devsecret")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@db:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "supersecretjwt")