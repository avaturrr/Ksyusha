"""Написать скрипт - таймер. Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут),
длину перерыва(по-умолчанию 5 минут), количество циклов(по-умолчанию 4)
и название задачи. Программа указывает оставшееся время фокусировки,
после сигнализирует о наступлении перерыва, после сигнализирует о начале нового цикла фокусировки.
Программа должна вести файл лога о всех запусках."""

import argparse
import time
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first_name", required=True)
parser.add_argument("-ln", "--last_name", required=True)
parser.add_argument("-ft", "--focus_time", default=25)
parser.add_argument("-rt", "--rest_time", default=5)
parser.add_argument("-ca", "--cycles_amount", default=4)
parser.add_argument("-tn", "--task_name", required=True)
args = parser.parse_args()
with open("log_info_scripts_07.txt", "a") as log_info:
    log_info.write(f"{args.first_name} {args.last_name} {datetime.now()} \n")

cycles_amount = int(args.cycles_amount)

for _ in range(cycles_amount):
    focus_time = int(args.focus_time)
    rest_time = int(args.rest_time)
    print("Now it's time for task")
    time.sleep(2)
    for _ in range(focus_time + 1):
        print(f"focus_time {focus_time}")
        time.sleep(60)
        focus_time -= 1
    print("Now it's time for rest")
    time.sleep(2)
    for _ in range(rest_time + 1):
        print(f"rest_time {rest_time}")
        time.sleep(60)
        rest_time -= 1
