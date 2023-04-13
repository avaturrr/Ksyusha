"""Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1), и False
в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
ных чисел. С помощью функции is_power_n найти количество степеней чис-
ла N в данном наборе.
"""
import math
from random import randint


def is_power_n(k: int, n: int):
    if math.log(k, n) % 1 == 0:
        return True
    else:
        return False


def main():
    number = int(input("Enter n: "))
    arr = [randint(1, 10) for i in range(10)]
    print(arr)
    count = 0
    for i in arr:
        if is_power_n(i, number):
            count += 1
    print(f"количество степеней {count}")


if __name__ == '__main__':
    main()
