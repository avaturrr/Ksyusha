"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n,
если n — нечетное; n!! = 2·4·6·...·n, если n — четное.
С помощью этой функции найти двойные факториалы пяти данных целых чисел"""

def my_func(n: int):
    list = [_ for _ in range(1, n + 1)]
    factorial = 1
    if n % 2 == 0:
        for i in list[1:n + 1:2]:
            factorial *= i
    else:
         for i in list[0:n+1:2]:
            factorial *= i
    return factorial
def main():
    factorial = my_func(3)
    print(factorial)
if __name__ == '__main__':
    main()

