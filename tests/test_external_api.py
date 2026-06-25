from unittest.mock import patch

from src.external_api import get_exchange_rate


@patch("requests.get")
def test_get_exchange_rate(mock_get):
    mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 74.77}}}
    assert get_exchange_rate() == {"Valute": {"USD": {"Value": 74.77}}}
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")
