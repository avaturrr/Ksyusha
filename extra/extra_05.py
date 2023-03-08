""""Есть список arr = [1,2,3,4,4,4,5,5,2]
Найти кумулятивную сумму"""

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
i = 0
cusum = []
sum = 0
while i < len(arr):
    sum += arr[i]
    cusum.append(sum)
    i +=1
print(cusum)