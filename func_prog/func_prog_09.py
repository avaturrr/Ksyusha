"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""
arr = ["alkdj", "jlkneli", "sldkjfo"]
my_dict = {(key + 1): value for key, value in enumerate(arr)}
print(my_dict)
