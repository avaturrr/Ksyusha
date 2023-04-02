"""Написать программу для нахождения факториала.
Факториал натурального числа n определяется
как произведение всех натуральных чисел от 1 до n включительно
"""
def funcs_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
def main():
    factorial = funcs_factorial(4)
    print(f"factorial = {factorial}")
if __name__ == '__main__':
   main()
