"""Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()

(подсказка: создается новый ключ с цифрой в конце, старый удаляется)

предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле.
"""
#c циклом for
my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
"""new_dict = {}
for key in my_dict.keys():
    value = my_dict[key]
    new_key = key + str(len(key))
    new_dict[new_key] = value
print(new_dict)"""
#с циклом while
new_dict = {}
i = 0
arr = list(my_dict.keys())
while i < len(arr):
    new_dict[arr[i] + str(len(arr[i]))] = my_dict.pop(arr[i])
    i += 1
print(new_dict)
