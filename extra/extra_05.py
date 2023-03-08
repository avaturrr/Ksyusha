""""Есть список arr = [1,2,3,4,4,4,5,5,2]
Найти массив квадратов"""

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
i = 0
sum = 1
while i < len(arr):
    sum = sum * arr[i]
    i +=1
print(sum ** (1 / len(arr)))