# Проект "transaction_analysis"

## Описание:
Проект "transaction_analysis" - это приложение для анализа транзакций, которые находятся в Excel-файле. Приложение генерирует JSON-данные для веб-страниц, формирует Excel-отчеты, а также предоставляет другие сервисы.

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/dmitryshvarev/transaction_analysis.git
```
Установите зависимости: 
```
pip install poetry
poetry install
poetry add pandas
poetry add openpyxl
poetry add requests
poetry add yfinance
```
## Тестирование:

- с помощью библиотеки pytest в проекте протестированы все модули
- все тесты выполнены успешно