"""
Условие задачи:
Пользователь вводит строку, проверить можно ли из нее сделать палиндром и вернуть его

Например:
Строка: Aab ba
Ее палиндром: baaab
Значит ответ: Да, можно

Строка: abc
Ответ: нельзя


Для решения задачи считаем кол-во для каждого символа (только буквы, не учитывая регистр) строки,
если нечетных значений > 1, то для строки нельзя сделать палиндром

Иначе находим символ, который будет стоять в центре (нечетное число) - middle
И добавляем к нему слева и справа все остальные символы по половине от общего количества этого символа
"""

from typing import Optional


def may_be_palindrome(any_string: str) -> Optional[str]:
    symbols_dict = {}
    for symbol in any_string:
        if symbol.isalpha():
            symbols_dict[symbol] = symbols_dict.get(symbol, 0) + 1

    odd_numbers = 0
    middle = ''
    for symbol, value in symbols_dict.items():
        if value % 2 != 0:
            middle = symbol
            odd_numbers += 1

        if odd_numbers > 1:
            return None

    pal = ''
    if middle:
        pal = middle * symbols_dict[middle]

    for symbol, value in symbols_dict.items():
        if symbol != middle:
            pal = ''.join((value // 2 * symbol, pal, value // 2 * symbol))

    return pal


user_string = input('Введите строку для проверки на палиндром: ')
palindrome = may_be_palindrome(user_string.lower())
if palindrome:
    print(f'Можно сделать палиндромом {palindrome}')
else:
    print('Нельзя сделать палиндромом')
