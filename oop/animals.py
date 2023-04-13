"""Создать файл animals.py. Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
oop_12
Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""


class Pet:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"Run {self.name}")

    def jump(self):
        print(f"Jump {self.name}")

    def birthday(self):
        self.age += 1

    def sleep(self):
        print(f"Sleep {self.name}")


class Dog(Pet):

    def bark(self):
        print(f"Bark {self.name}")


class Cat(Pet):

    def meow(self):
        print(f"Meow {self.name}")


class Parrot(Pet):

    def fly(self):
        print(f"Fly {self.name}")


dog_01 = Dog("a", 3, "AF")
dog_01.bark()
dog_01.jump()
dog_01.sleep()
dog_01.run()
dog_01.birthday()
print(dog_01.age)

cat_01 = Cat("c", 2, "CF")
cat_01.meow()
cat_01.jump()
cat_01.sleep()
cat_01.run()
cat_01.birthday()
print(cat_01.age)

parrot_01 = Parrot("f", 25, "FF")
parrot_01.fly()
parrot_01.jump()
parrot_01.sleep()
parrot_01.run()
parrot_01.birthday()
print(parrot_01.age)
