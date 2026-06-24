import requests


def get_exchange_rate() -> dict:
    """Запрашивает информацию курса обмена валют у внешнего API"""
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    return response.json()
