import os
import yfinance as yf
import json

from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Union

from utils import get_transactions_for_analysis, amount_in_rub, get_settings
from src.external_api import get_exchange_rate

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


def get_cards_info(user_date: str) -> List[Dict[str, Union[str, float]]]:
    """Возвращает информацию по используемым банковским картам"""
    transactions = get_transactions_for_analysis(os.path.abspath(r"..\data\operations.xlsx"), user_date)

    totals = defaultdict(float)
    for transaction in transactions:
        if transaction.get('Номер карты') and transaction.get('Статус') == 'OK' and transaction.get('Сумма платежа') < 0:
            totals[transaction['Номер карты']] += abs(amount_in_rub(transaction))

    cards = []
    for card_num, total_spent in totals.items():
        card = dict()
        card['last_digits'] = card_num[-4:]
        card['total_spent'] = round(total_spent, 2)
        card['cashback'] = round(total_spent * 0.01, 2)

        cards.append(card)

    return cards


def get_top_transactions(user_date: str) -> List[Dict[str, Union[str, float]]]:
    """Возвращает топ-5 транзакций, отсортированных по убыванию суммы"""
    transactions = get_transactions_for_analysis(os.path.abspath(r"..\data\operations.xlsx"), user_date)

    top_5_largest = sorted(transactions, key=lambda x: abs(amount_in_rub(x)), reverse=True)[:5]

    top_transactions = []
    for transaction in top_5_largest:
        top_transaction = dict()
        top_transaction['date'] = transaction.get('Дата операции')[:10]
        top_transaction['amount'] = transaction.get('Сумма платежа')
        top_transaction['category'] = transaction.get('Категория')
        top_transaction['description'] = transaction.get('Описание')

        top_transactions.append(top_transaction)

    return top_transactions


def get_currency_rates() -> List[Dict[str, Union[str, float]]]:
    currencies = get_settings('../user_settings.json')['user_currencies']
    exchange_rate = get_exchange_rate()

    currency_rates = []
    for currency in currencies:
        currency_rate = dict()
        currency_rate['currency'] = currency
        currency_rate['rate'] = round(exchange_rate["Valute"][currency]["Value"], 2)

        currency_rates.append(currency_rate)

    return currency_rates


def get_stock_prices() -> List[Dict[str, Union[str, float]]]:
    """Возвращает цены на акции"""
    stocks = get_settings('../user_settings.json')['user_stocks']

    stock_prices = []
    for stock in stocks:
        stock_price = dict()
        stock_price['stock'] = stock
        stock_price['price'] = round(yf.Ticker(f'{stock}').info.get('currentPrice'), 2)

        stock_prices.append(stock_price)

    return stock_prices


def get_home_page_info(user_date: str) -> str:
    """Возвращает JSON c информацией о транзакциях для главной страницы """
    home_page = dict()
    home_page["greeting"] = greeting(user_date)
    home_page["cards"] = get_cards_info(user_date)
    home_page["top_transactions"] = get_top_transactions(user_date)
    home_page["currency_rates"] = get_currency_rates()
    home_page["stock_prices"] = get_stock_prices()

    home_page_json = json.dumps(home_page, indent=4, ensure_ascii=False)

    return home_page_json


#if __name__ == '__main__':
    #print(get_home_page_info("2020-05-20 06:00:00"))
    # print(greeting("2020-05-20 06:00:00"))
    # print(get_cards_info("2019-04-30 13:30:00"))
    # print(get_top_transactions("2019-04-30 13:30:00"))
    # print(get_currency_rates())
    # print(get_stock_prices())
