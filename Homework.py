# Функция, которая возвращает сумму двух чисел
def add_numbers(a, b):
    return a + b
# Тест 1: проверка, что функция возвращает правильную сумму положительных чисел
def test_add_positive_numbers():
    assert add_numbers(3, 5) == 8

# Тест 2: проверка, что функция возвращает правильную сумму отрицательных чисел
def test_add_negative_numbers():
    assert add_numbers(-3, -5) == -8

# Тест 3: проверка, что функция возвращает правильную сумму положительного и отрицательного числа
def test_add_mixed_numbers():
    assert add_numbers(3, -5) == -2