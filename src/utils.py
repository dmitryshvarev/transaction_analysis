from datetime import datetime
from openpyxl import load_workbook
from typing import Dict, List, Union


def get_transactions_for_analysis(file_path: str, user_date: str) -> List[Dict[str, Union[str, float, int]]]:
    """Получаем данные о финансовых операциях с начала месяца по user_date"""
    wb = load_workbook(file_path, read_only=True, data_only=True)
    ws = wb.active

    rows = ws.iter_rows(values_only=True)
    headers = next(rows)

    transactions = []

    user_datetime: datetime = datetime.strptime(user_date, "%Y-%m-%d %H:%M:%S")
    start_of_month = datetime(user_datetime.year, user_datetime.month, 1)

    for row in rows:
        row_dict = dict(zip(headers, row))
        trans_date = row_dict.get("Дата операции")
        if trans_date:
            trans_date = datetime.strptime(trans_date, "%d.%m.%Y %H:%M:%S")

        # Фильтруем записи: от начала месяца до пользовательской даты включительно
        if start_of_month <= trans_date <= user_datetime:
            transactions.append(row_dict)

    wb.close()
    return transactions


if __name__ == '__main__':
    print(get_transactions_for_analysis(r"..\data\operations.xlsx", "2018-01-03 15:00:00"))
