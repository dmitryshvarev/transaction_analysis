import json
import re

from typing import Dict, List, Union


def phone_number_search(transactions_being_analyzed: List[Dict[str, Union[str, float, int]]]) -> str:
    """Возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера"""
    pattern = r"\+7\s9\d{2}\s\d{2,3}-\d{2}-\d{2}"

    transactions_phone = [transaction for transaction in transactions_being_analyzed if re.search(pattern, transaction.get("Описание"))]

    return json.dumps(transactions_phone, indent=4, ensure_ascii=False)
