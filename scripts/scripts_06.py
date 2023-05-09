"""Написать скрипт - таймер. Программа при запуске принимает
имя, фамилию, часы, минуты и секунды. После программа начинает
обратный отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда."""

import argparse
import time
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-ftn", "--first_name", required=True)
parser.add_argument("-ltn", "--last_name", required=True)
parser.add_argument("-hs", "--hours", required=True)
parser.add_argument("-ms", "--minutes", required=True)
parser.add_argument("-ss", "--seconds", required=True)
args = parser.parse_args()
args.seconds = int(args.seconds)
args.minutes = int(args.minutes)
args.hours = int(args.hours)
for _ in range(args.hours + 1):
    for _ in range(args.minutes + 1):
        for _ in range(args.seconds + 1):
            print(f"{args.hours}:{args.minutes}:{args.seconds}")
            args.seconds -= 1
            time.sleep(1)
        args.seconds = 60
        args.minutes -= 1
    args.minutes = 60
    args.hours -= 1
with open("log_info.txt", "a") as log_info:
    log_info.write(f"{datetime.now()} {args.first_name} {args.last_name}\n")
