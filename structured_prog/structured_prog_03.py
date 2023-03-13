"""Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки"""

sum_rub = int(input("Enter sum rub:"))
sum_cop = int(input("Enter sum cop"))
if sum_cop != 0 and sum_rub != 0:
    print(f"{sum_rub} руб {sum_cop} коп")
elif sum_cop == 0 and sum_rub != 0:
    print(f"{sum_rub} руб")
elif sum_rub == 0 and sum_cop != 0:
    print(f"{sum_cop} коп")
else:
    print("0")