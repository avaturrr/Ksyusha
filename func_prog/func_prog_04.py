"""Дан словарь, создать новый словарь, поменяв местам ключ и значение
"""

my_dict = {"number": 2, "year": 2009, "number1": 1, "year1": 2000, "number2": 4, "year3": 2004}
new_dict = {value: key for key, value in my_dict.items()}
print(new_dict)
