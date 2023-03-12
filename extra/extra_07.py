""""Есть список arr = [1,2,3,4,4,4,5,5,2]
айти верхнюю и нижнюю квартиль"""

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
i = 0
j = 0
ordered_arr = []
while len(arr) != 0:
    while (arr[j] <= arr[i]):
        i += 1
        if i == len(arr):
            ordered_arr.append(arr.pop(j))
            i = 0
            break
    j = i
print(ordered_arr)
up_q = 0.75 * (len(ordered_arr) + 1)
down_q = 0.25 * (len(ordered_arr) + 1)
if up_q % 1 == 0:
    print(f"Верхний квартиль: {ordered_arr[int(up_q // 1)]}")
else:
    print(f"Верхний квартиль: {(ordered_arr[int(up_q // 1 - 1)] + ordered_arr[int(up_q // 1)]) / 2}")
if down_q % 1 == 0:
    print(f"Нижний квартиль: {ordered_arr[int(down_q // 1)]}")
else:
    print(f"Нижний квартиль: {(ordered_arr[int(down_q // 1 - 1)] + ordered_arr[int(down_q // 1)]) / 2}")