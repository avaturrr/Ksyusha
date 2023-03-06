"""В заданной строке расположить в обратном порядке
все слова.
Разделителями слов считаются пробелы."""

my_str = input("Enter line: ")
my_str = my_str.split(" ")
my_str = my_str[::-1]
my_str = " ".join(my_str)
print(my_str)