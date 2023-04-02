"""Создать универсальный декоратор,
который меняет порядок аргументов в функции на противоположный. """
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def inner(*args):
        args = args[::-1]
        new_func = func(args)
        return new_func

    return inner


def my_func(*args):
    return args


def main():
    a = my_decorator(my_func)
    arr = a(1, 2, 3, 4)
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
