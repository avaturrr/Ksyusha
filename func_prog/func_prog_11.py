"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""


def my_func(*args):
    return (args)


def my_decorator(func):
    def my_inner(*args):
        my_list = [i for i in func(*args) if i % 2 == 1]
        return my_list
    return my_inner


def main():
    a = my_decorator(my_func)
    b = a(1, 2, 3, 4)
    print(b)


if __name__ == "__main__":
    main()
