from src.utils import amount_in_rub, get_settings, get_transactions_for_analysis


def test_get_transactions_for_analysis(transactions_for_analysis):
    assert (
        get_transactions_for_analysis(r"..\data\operations.xlsx", "2021-12-01 13:00:00") == transactions_for_analysis
    )


def test_amount_in_rub(transactions_for_analysis):
    assert amount_in_rub(transactions_for_analysis[0]) == -99.0


def test_get_settings(settings):
    assert get_settings("../user_settings.json") == settings
