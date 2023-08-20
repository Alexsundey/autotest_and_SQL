﻿# Автоматизация теста к API.
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.
   Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- ![2023-08-18_00-23-56.png](..%2F..%2FDownloads%2F2023-08-18_00-23-56.png)
# Запросы SQL
![2023-08-20_15-54-53.png](..%2F..%2FDownloads%2F2023-08-20_15-54-53.png)