def is_palindrome(s):
    """
    Функция проверяет, является ли строка палиндромом.

    Алгоритм:
    1. Привести строку к нижнему регистру (чтобы не учитывать разницу между заглавными и строчными буквами).
    2. Удалить из строки все пробелы, знаки препинания и другие ненужные символы (если требуется).
    3. Перевернуть строку.
    4. Сравнить исходную обработанную строку с её перевёрнутым вариантом.
    5. Если строки совпадают — вернуть True (строка является палиндромом), иначе вернуть False.
    """

    # Приводим строку к нижнему регистру
    s = s.lower()

    # Убираем все не буквенно-цифровые символы (если требуется)
    s = ''.join(c for c in s if c.isalnum())

    # Проверяем, равна ли строка своему перевёрнутому варианту
    return s == s[::-1]


# Тестирование функции
print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("12321"))  # True
print(is_palindrome("Python"))  # False
