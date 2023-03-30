"""Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
file_read = file.read()
list_line = file_read.split()
print(f"a {list_line[0]}")
print(f"b {list_line[4]}")
print(f"c {list_line[0:5]}")
print(f"d {list_line[0:2]}")
print(f"e {list_line}")
file.close()

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
count = 0
while line := file.readline():
    if count == 0:
        print(f"a {line}")
        break
file.close()

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
count = 0
while line := file.readline():
    if count == 5:
        print(f"b {line}")
        break
    count += 1
file.close()

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
count = 0
my_list = []
while line := file.readline():
    if 0 <= count < 5:
        my_list.append(line.strip())
    count += 1
print(f"c {my_list}")
file.close()

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
count = 0
my_list = []
while line := file.readline():
    if 0 <= count < 2:
        my_list.append(line.strip())
    count += 1
print(f"d {my_list}")
file.close()

file = open("/home/user/PycharmProjects/Ksyusha/files/test.txt")
my_list = []
while line := file.readline():
    my_list.append(line.strip())
print(f"e {my_list}")
file.close()
