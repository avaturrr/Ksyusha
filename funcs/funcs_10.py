"""Написать функцию по решению квадратных уравнений."""

def my_func(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Нет корней")
    elif d == 0:
        x = - b / (2 * a)
        return x
    else:
        x_1 = (-b + d ** (1 / 2)) / (2 * a)
        x_2 = (-b - d ** (1 / 2)) / (2 * a)
        return x_1, x_2
def main():
    x = my_func(1, - 4, - 5)
    print(f"{x}")
if __name__ == '__main__':
   main()
