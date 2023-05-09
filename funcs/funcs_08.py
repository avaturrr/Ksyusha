"""Написать функцию принимающая на вход неопределенным количеством аргументов
и именованный аргумент mean_type. В зависимости от mean_type вернуть среднеарифметическое
либо среднегеометрическое. Написать программу в виде трех функций."""


def my_funcs_srar(*args):
    sum = 0
    for i in args:
        sum += i
    sum = sum / len(args)
    return sum


def my_funcs_srg(*args):
    sum = 1
    for i in args:
        sum *= i
    sum = sum ** (1 / len(args))
    return sum


def my_function(*args, mean_type=0):
    if mean_type == 0:
        return my_funcs_srar(*args)
    elif mean_type == 1:
        return my_funcs_srg(*args)


def main():
    sum = my_function(4, 4, 2, 2, mean_type=0)
    print(f"sum = {sum}")


if __name__ == '__main__':
    main()
