"""Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while"""

n = int(input("Enter number: "))
i = 0
sum_3 = 0
while i <= n:
    sum_3 += i ** 3
    i += 1
print(sum_3)