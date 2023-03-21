"""Создать функцию, которая принимает на вход неопределенное количество аргументов
и возвращает их сумму и максимальное из них."""
def funcs_sum_max(*args):
    sum = 0
    for i in args:
        sum += i
    args_max = max(args)
    return sum, args_max
def main():
    sum, my_max = funcs_sum_max(2, 3, 6, 8)
    print(f"sum = {sum}, max = {my_max}")
if __name__ == '__main__':
   main()
