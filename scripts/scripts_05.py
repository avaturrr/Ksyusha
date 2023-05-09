"""Создать скрипт. Программа принимает имя папки
и имя файла с расширением. Создает папку и создает в ней файл.
Если расширение файла py - записывает в файл следующее: """

import os.path
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-nd", "--name_dir", required=True)
parser.add_argument("-nf", "--name_file", required=True)
args = parser.parse_args()
scripts_path = os.path.dirname(os.path.realpath("scripts_04.py"))
dir_path = os.path.join(scripts_path, args.name_dir)
os.mkdir(dir_path)
with open(os.path.join(dir_path, args.name_file), "w+") as my_file:
    if str(args.name_file[len(args.name_file) - 2::]) == "py":
        my_file.write("def main():\n    pass\nif __name__ == '__main__':\n    main()")
