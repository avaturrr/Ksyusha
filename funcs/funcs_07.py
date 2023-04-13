"""Создать функцию, которая принимает на вход неопределенное количество
именованных аргументов и выводит на экран те из них, длина ключа которых четна.
"""
def my_funcs(**kwargs):
    filtred_dict = {}
    for key in kwargs.keys():
        if len(key) % 2 == 0:
            filtred_dict[key] = kwargs[key]
    return filtred_dict
def main():
    my_dict = my_funcs(akdj = 1, jfa = 34, j0ekd = 6)
    print(f"filtred dict = {my_dict}")
if __name__ == '__main__':
   main()
