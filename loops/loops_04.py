"""Просуммировать неопределенное количество чисел, вводимых пользователем,
суммировать до тех пор, пока пользователь не введёт слово «стоп».
Не учитывать числа кратные 5"""

sum = 0
while True:
    i = input("Enter number or stop: ")
    if i == "stop":
        break
    else:
        if int(i) % 5 != 0:
            sum += int(i)
            print(f"sum = {sum}")
        else:
            continue