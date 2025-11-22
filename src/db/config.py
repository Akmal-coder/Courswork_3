import os
from typing import Dict


def get_db_params() -> Dict[str, str]:
    """
    Возвращает параметры подключения к БД из переменных окружения
    """
    return {
        "dbname": os.getenv("DB_NAME", "hh_vacancies"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "Akmal1717"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
    }
