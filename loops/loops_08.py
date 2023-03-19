"""Ввести два целых числа a и b ( a < b ).
Вывести в порядке возрастания все целые числа,
расположенные между a и b (включая сами числа a и b ),
а также количество n этих чисел."""

a = int(input("Enter start number: "))
b = int(input("Enter stop number: "))
my_list = []
count = 0
for i in range(a, b + 1):
    my_list.append(i)
    count += 1
print("list {}, amount {}".format(my_list, count))