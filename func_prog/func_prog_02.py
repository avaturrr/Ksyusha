"""Дан список слов. Сгенерировать новый список с перевернутыми словами
"""

my_list = ["alsdkfj", "dlksj", "alj"]
new_list = [i[::-1] for i in my_list]
print(new_list)