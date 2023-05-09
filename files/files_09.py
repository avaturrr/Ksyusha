"""Использовать результаты files_08. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в files_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
from csv_utils import *

# 1
cost_goods = my_sum("my_csv.csv")
print(f"sum goods {cost_goods}")
# 2
max_cost = max_price("my_csv.csv")
print(f"max {max_cost}")
# 3
min_cost = min_price("my_csv.csv")
print(f"min {min_cost}")
# 4
minus = delete_amount("my_csv.csv", 2)
