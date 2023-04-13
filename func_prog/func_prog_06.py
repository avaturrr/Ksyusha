"""Дан список имен, отфильтровать все имена, где есть буква o

[‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]
"""

my_list = ["Kate", "Kolya", "Alex"]
new_list = list(filter(lambda name: "o" in name, my_list))
print(new_list)
