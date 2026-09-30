import psycopg2

from config import DB_CONFIG


def get_connection():
    """Создаёт и возвращает подключение к PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)
