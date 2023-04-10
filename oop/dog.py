"""oop_01
Создать файл dog.py.
Создать пустой класс Dog
oop_02
Создать два объекта класса Dog. Вывести их на экран
"""


class Dog:
    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")


dog_1 = Dog()
dog_1.run()
dog_1.jump()
dog_2 = Dog()
dog_2.jump()
dog_2.run()
print(dog_1)
print(dog_2)
