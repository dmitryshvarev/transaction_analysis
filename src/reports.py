import pandas as pd

from datetime import datetime, timedelta
from typing import Optional

from decorators import write_report


@write_report("report")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if not date:
        date = "31.12.2021"
    date_finish = datetime.strptime(date, "%d.%m.%Y")
    date_start = date_finish - timedelta(days=90)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"])
    mask = (
        (date_start <= transactions["Дата операции"])
        & (transactions["Дата операции"] <= date_finish)
        & (transactions["Категория"] == category)
    )
    return transactions[mask]
