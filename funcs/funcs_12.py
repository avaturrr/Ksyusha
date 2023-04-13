"""Дан массив целых чисел A. Найти суммы положительных и отрицательных элементов массива,
используя функцию определения суммы. """
from random import randint
def f_sum(arr):
    sum_plus = 0
    sum_minus = 0
    for arr_01 in arr:
        for i in arr_01:
            if i < 0:
                sum_minus += i
            else:
                sum_plus += i
    return sum_plus, sum_minus
def main():
    matrix = [[randint(-10, 10) for _ in range(3)] for _ in range(3)]
    sum_plus_minus = f_sum(matrix)
    print(matrix)
    print(f"{sum_plus_minus}")
if __name__ == '__main__':
   main()
