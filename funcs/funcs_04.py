"""Реализовать функцию возвращающую матрицу.
На вход принимает n - размерность матрицы,
random_from(по-умолчанию 1), random_to(по-умолчанию(9))."""
from random import randint
def new_matrix(n: int, random_from = 1, random_to = 9):
    matrix = [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]
    return matrix
def main():
    matrix = new_matrix(4)
    print(f"matrix = {matrix}")
if __name__ == '__main__':
   main()
