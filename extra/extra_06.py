""""Есть список arr = [1,2,3,4,4,4,5,5,2]
Найти медиану"""

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
i = 0
j = 0
ordered_arr = []
while len(arr) != 0:
    while (arr[j] <= arr[i]):
        i += 1
        if i == len(arr):
            ordered_arr.append(arr.pop(j))
            break
    if j < len(arr) - 1: #я думала, может j присваивать тут рандомное число. но ничего не получилось
        j += 1
    else:
        j = 0
    i = 0
print(ordered_arr)
if len(ordered_arr) % 2 == 0:
    mediana = (ordered_arr[int((len(ordered_arr) / 2) - 1)] + ordered_arr[int((len(ordered_arr) / 2 + 1) - 1)]) / 2
    print(mediana)
else:
    mediana = ordered_arr[int((len(ordered_arr) + 1) / 2) - 1]
    print(mediana)