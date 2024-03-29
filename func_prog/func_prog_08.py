"""Написать декоратор, который будет выводить время выполнения функции
from datetime import datetime
time = datetime.now()
"""
from datetime import datetime
from functools import wraps
from random import randint


def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.now()
        delta = finish_time - start_time
        print(delta)
        return result

    return inner


@my_decorator
def very_importent_func(arr):
    from time import sleep
    arr = list(map(lambda x: x * 2, arr))
    print(arr)
    return arr


arr = [i for i in range(100)]
very_importent_func(arr)
