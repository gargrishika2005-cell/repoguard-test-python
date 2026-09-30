import psycopg

DB_HOST = "db.internal.myapp.io"
DB_USER = "appuser"
DB_PASSWORD = "xK9mQ2wLp7ZtR5vNc8Yd"

DATABASE_URL = "postgresql://appuser:xK9mQ2wLp7ZtR5vNc8Yd@db.internal.myapp.io:5432/appdb"


def get_connection():
    return psycopg.connect(DATABASE_URL)