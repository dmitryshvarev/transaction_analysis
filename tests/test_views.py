from src.views import get_cards_info, get_top_transactions, greeting


def test_greeting():
    assert greeting("2020-05-20 06:00:00") == "Доброе утро"
    assert greeting("2020-05-20 12:00:00") == "Добрый день"
    assert greeting("2020-05-20 18:00:00") == "Добрый вечер"
    assert greeting("2020-05-20 23:00:00") == "Доброй ночи"


def test_get_cards_info(cards_info):
    assert get_cards_info("2019-04-30 13:30:00") == cards_info


def test_get_top_transactions(top_transactions):
    assert get_top_transactions("2019-04-30 13:30:00") == top_transactions
