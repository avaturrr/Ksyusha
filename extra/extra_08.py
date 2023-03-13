
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if  arr[i] > arr [j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

arr_01 = [7, 2, 3, 10, 4, 4, 5, 5, 2]
i = 0
j = 0
while i < len(arr_01):
    while j < len(arr_01):
        if arr_01[i] < arr_01[j]:
            arr_01[i], arr_01[j] = arr_01[j], arr_01[i]
        j += 1
    j = 0
    i += 1
print(arr_01)
