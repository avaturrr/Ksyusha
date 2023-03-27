"""Написать декоратор, который будет выводить время выполнения функции
from datetime import datetime
time = datetime.now()
"""
from datetime import datetime
from functools import wraps


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
    from time import sleep
    arr = list(map(lambda ))

very_important_func()
