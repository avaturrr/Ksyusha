"""Просуммировать неопределенное количество чисел, вводимых пользователем,
суммировать до тех пор, пока пользователь не введёт слово «стоп»"""

sum = 0
while True:
    i = input("Enter number or stop: ")
    if i == "stop":
        break
    else:
        sum += int(i)
        print(f"sum = {sum}")