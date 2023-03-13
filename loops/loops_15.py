"""Написать игру. Пользователь должен угадать число.
Сперва вводится диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано -
выводить: You are the loser и правильное число."""

start_range = int(input("Enter start range number: "))
final_range = int(input("Enter final range number: "))
amount_attempts = int(input("Enter amount attempts: "))
from random import randint
number = randint(start_range, final_range)
for i in range(1, amount_attempts + 1):
    attempt = int(input("Enter your number: "))
    if attempt == number:
        print("You are winner")
        break
    elif attempt < number:
        print("Искомое число больше")
    else:
        print("Искомое число меньше")
else:
    print("You are loser")