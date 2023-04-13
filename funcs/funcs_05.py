"""Создать функцию, принимающая на вход неопределенное количество аргументом
и возвращающая сумму args[i] * i
Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""
def funcs_sum_args(*args):
    sum = 0
    for index, item in enumerate(args):
        sum += index * item
    return sum
def main():
    sum = funcs_sum_args(1, 3, 4)
    print(f"sum = {sum}")
if __name__ == '__main__':
   main()
