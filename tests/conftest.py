import pytest


@pytest.fixture
def transactions_for_analysis():
    return [
        {
            "Дата операции": "01.12.2021 12:35:05",
            "Дата платежа": "01.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -99.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -99.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Фастфуд",
            "MCC": 5814.0,
            "Описание": "IP Yakubovskaya M.V.",
            "Бонусы (включая кэшбэк)": 1.0,
            "Округление на инвесткопилку": 0.0,
            "Сумма операции с округлением": 99.0,
        }
    ]


@pytest.fixture
def settings():
    return {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}


@pytest.fixture
def cards_info():
    return [
        {"last_digits": "4556", "total_spent": 20522.62, "cashback": 205.23},
        {"last_digits": "7197", "total_spent": 25011.6, "cashback": 250.12},
    ]


@pytest.fixture
def top_transactions():
    return [
        {
            "date": "22.04.2019",
            "amount": 34601.15,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {
            "date": "22.04.2019",
            "amount": -34601.15,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {
            "date": "30.04.2019",
            "amount": 26100.0,
            "category": "Зарплата",
            "description": 'Пополнение. ООО "ФОРТУНА". Зарплата',
        },
        {
            "date": "15.04.2019",
            "amount": 26100.0,
            "category": "Зарплата",
            "description": 'Пополнение. ООО "ФОРТУНА". Аванс',
        },
        {"date": "22.04.2019", "amount": 1036.17, "category": "Переводы", "description": "Перевод между счетами"},
    ]
