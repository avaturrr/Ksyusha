""""Есть список arr = [1,2,3,4,4,4,5,5,2]
Найти медиану"""

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
if len(arr) % 2 == 0:
    mediana = (arr[int((len(arr) / 2) - 1)] + arr[int((len(arr) / 2 + 1) - 1)]) / 2
    print(mediana)
else:
    mediana = arr[int((len(arr) + 1) / 2) - 1]
    print(mediana)