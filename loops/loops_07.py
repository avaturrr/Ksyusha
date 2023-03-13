"""Получить сумму кубов натуральных чисел от n до m, используя цикл for"""

n = int(input("Enter start number: "))
m = int(input("Enter stop number: "))
sum = 0
for i in range(n, m +1):
    sum += i ** 3
print(sum)