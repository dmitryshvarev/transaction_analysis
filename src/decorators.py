from functools import wraps
from typing import Any, Callable, Optional


def write_report(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """
    Фабрика декораторов. Принимает параметр декоратора и возвращает сам декоратор.

    :param filename: Название файла, куда будет записываться вывод работы декоратора.
                     Если не передаётся, информация выводится в консоль.
    :return: Декоратор, который оборачивает исходную функцию.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)  # Сохраняет docstring и __name__ оригинальной функции
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка для декорируемой функции.
            Записывает результат функции в файл или выводит в консоль.
            """
            result = func(*args, **kwargs)

            if filename:
                with open(f"../{filename}", "a", encoding="UTF-8") as file:
                    result.to_excel(f"../{filename}.xlsx")
            else:
                print(result)

            return result

        return wrapper

    return decorator
