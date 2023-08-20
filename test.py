import create_orders_test

# Воробьев Александр, 7-я когорта — Финальный проект. Инженер по тестированию плюс

def test_get_orders_assert():
    user_response = create_orders_test.get_orders()
    if user_response.status_code == 200:
        print('Тест пройден')
    else:
        print('Тест провален')

