"""Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
Создать новый список со всеми машинами, год выпуска которых больше n"""

my_list = [
    {"number": 1, "year": 2009},
    {"number": 1, "year": 2000},
    {"number": 1, "year": 2004},
    {"number": 1, "year": 2002}
]

n = 2003
new_list = [dict_element for dict_element in my_list if dict_element["year"] > n]
print(new_list)