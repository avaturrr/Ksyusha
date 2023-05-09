"""Создать файл time.py. Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Переопределить магические методы сравнения(равно, не равно), сложения, вычитания, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида: одна строка, три числа, другой объект класса MyTime.
В остальных случаях создавать объект по-умолчанию(0-0-0)
"""


class MyTime:
    def __init__(self, *args):
        if isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif isinstance(args[0], str):
            separ_str = args[0].split()
            self.hours = separ_str[0]
            self.minutes = separ_str[1]
            self.seconds = separ_str[2]
        elif isinstance(args[0], type(self)):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes \
                and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if not (self.hours == other.hours and self.minutes == other.minutes
                and self.seconds == other.seconds):
            return True
        else:
            return False

    def __add__(self, other):
        sum_sec = self.seconds + other.seconds + (self.minutes + other.minutes) * 60 + \
                  (self.hours + other.hours) * 3600
        s = sum_sec % 60
        h = sum_sec // 3600
        m = (sum_sec - h * 3600) // 60
        return MyTime(h, m, s)

    def __sub__(self, other):
        sub_sec = self.seconds - other.seconds + (self.minutes - other.minutes) * 60 + \
                  (self.hours - other.hours) * 3600
        s = sub_sec % 60
        h = sub_sec // 3600
        m = (sub_sec - h * 3600) // 60
        return MyTime(h, m, s)

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes {self.seconds} seconds"


def main():
    time_1 = MyTime(1, 30, 40)
    time_2 = MyTime(2, 20, 55)
    time_3 = time_2 + time_1
    print(time_1 == time_2)
    print(time_3)

    time_4 = MyTime(1, 30, 14)
    print(time_4)
    time_5 = MyTime("5 7 2")
    print(time_5)
    time_6 = MyTime(time_4)
    print(time_6)



if __name__ == "__main__":
    main()
