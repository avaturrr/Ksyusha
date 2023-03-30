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
        return result

    return inner


@my_decorator
def very_important_func(arr):
    arr = list(map(lambda i: i * 2, arr))
    return arr


very_important_func([randint(1, 20) for i in range(20)])
print(very_important_func)
