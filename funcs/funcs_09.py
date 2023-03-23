"""Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать функцию.
Подсказка: для хранения данных использовать словарь. Для проверки нахождения элемента
в словаре использовать метод get(), либо оператор in
"""

def my_func(*args):
    my_set = set(args)
    my_dict = {}
    for j in my_set:
        count = 0
        for i in args:
            if j == i:
                count += 1
        my_dict[j] = count
    return my_dict

def main():
    my_dict = my_func(1, 2, 3, 4, 5, 3, 5, 4, 4, 4)
    print(f"{my_dict}")
if __name__ == '__main__':
   main()
