"""В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""

with open("test3.txt", "a") as my_file:
    for line in range(3):
        my_file.writelines([input("Enter line: ")])
        my_file.write("\n")
