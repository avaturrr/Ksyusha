"""Написать функцию по переводу:
Дюймы в сантиметры, Сантиметры в дюймы, Мили в километры, Километры в мили, Фунты в килограммы,
Килограммы в фунты, Унции в граммы, Граммы в унции, Галлон в литры, Литры в галлоны,
Пинты в литры, Литры в пинты
Примечание: функция принимает на вход число, и коэффициент, возвращает конвертированное число.
Для хранения коэффициент использовать словарь

Написать программу, со следующим интерфейсом: пользователю предоставляется на выбор
12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру от одного до двенадцати.
После программа запрашивает ввести численное значение. Затем программа выдает конвертированный результат.
Использовать функцию из первого задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""


def my_funcs(number, option):
    my_dict = {"1": 2.54, "2": 0.393701, "3": 1.852, "4": 0.539957}
    result = number * my_dict[option]
    return result


def main():
    while True:
        number = int(input("Enter number: "))
        option = input("Enter option: ")
        if option == "0":
            break
        result = my_funcs(number, option)
        print(f"{result}")


if __name__ == '__main__':
    main()