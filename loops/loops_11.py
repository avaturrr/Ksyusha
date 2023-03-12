"""Дан двумерный массив n × m элементов.
Определить, сколько раз встречается число 7 среди элементов массива."""

n = int(input("Enter number n: ")) #в задании список ДАН.я сначала создала, потом искала 7
m = int(input("Enter number m: "))
my_list = []
my_list_in = []
from random import randint
for i in range(1, m + 1):
    for j in range(1, n + 1):
        my_list_in.append(randint(1, 9))
    my_list.append(list(my_list_in))
    my_list_in = []
print(my_list)
count_7 = 0
for a in my_list:
    for b in list(a):
        if b == 7:
            count_7 += 1
print(f"Amount 7: {count_7}")

