"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n**2 for n in numbers]


def is_prime(n):
    den = 2
    if n > 1:
        while n % den != 0:
            den = den + 1
        if den == n:
            return True
        else:
            return False
    else:
        return False


def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# filter types
ODD = is_odd
EVEN = is_even
PRIME = is_prime


def filter_numbers(numbers, ft):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    return list(filter(ft, numbers))
