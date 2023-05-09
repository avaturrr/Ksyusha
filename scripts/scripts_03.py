"""Создать скрипт, который принимает имя папки
и создает ее рядом со скриптом"""
import os
import sys

args = sys.argv
script_path = os.path.dirname(os.path.realpath("scripts_03.py"))
new_dir_path = str(script_path) + "/" + args[1]
os.mkdir(new_dir_path)
