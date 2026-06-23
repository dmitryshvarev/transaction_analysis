from datetime import datetime

from utils import get_transactions_for_analysis


def greeting(user_date: str) -> str:
    """Возвращает приветствие, соответствующее времени суток"""
    user_hour = datetime.strptime(user_date, "%Y-%m-%d %H:%M:%S").hour
    if 6 <= user_hour < 12:
        return "Доброе утро"
    elif 12 <= user_hour < 18:
        return "Добрый день"
    elif 18 <= user_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def cards_info():
    pass


if __name__ == '__main__':
    print(greeting("2020-05-20 06:00:00"))
