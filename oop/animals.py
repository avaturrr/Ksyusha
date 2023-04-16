"""Создать файл animals.py. Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
oop_12
Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
oop_13
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один параметр
и прибавляющий его к соответствующему аргументу. В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение This parrot cannot fly.
oop_14
Переопределить методы change_weight, change_height в классе Parrot.
В случае непередачи параметра - вес изменяется на 0.05
oop_16
Добавить в класс Parrot  новый атрибут - species
oop_17
Добавить в класс Pet пустой метод voice. Заменить имена методов bark, meow на voice.
Добавить voice для класса Parrot.
Создать функцию, принимающую список животных и вызывающую у каждого животного метод voice.

"""


class Pet:

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def change_weight(self, number=None):
        if number:
            self.weight += number
        else:
            self.weight += 0.2

    def change_height(self, number=None):
        if number:
            self.height += number
        else:
            self.height += 0.2

    def run(self):
        print(f"Run {self.name}")

    def jump(self):
        print(f"Jump {self.name}")

    def birthday(self):
        self.age += 1

    def sleep(self):
        print(f"Sleep {self.name}")

    def new_jump(self, jump_height):
        print(f"Jump {jump_height} meters")

    def voice(self):
        pass


class Dog(Pet):

    def voice(self):
        print(f"Bark {self.name}")

    def new_jump(self, jump_height):
        if jump_height > 0.5:
            print("Dogs cannot jump so high")
        else:
            super().new_jump(jump_height)


class Cat(Pet):

    def voice(self):
        print(f"Meow {self.name}")

    def new_jump(self, jump_height):
        if jump_height > 2:
            print("Cats cannot jump so high")
        else:
            super().new_jump(jump_height)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print(f"Fly {self.name}")

    def change_weight(self, number=None):
        if number:
            self.weight += number
        else:
            self.weight += 0.5

    def change_height(self, number=None):
        if number:
            self.height += number
        else:
            self.height += 0.5

    def new_jump(self, jump_height):
        if jump_height > 0.05:
            print("Parrots cannot jump so high")
        else:
            super().new_jump(jump_height)

    def voice(self):
        print(f"AAAAA {self.name}")

dog_01 = Dog("a", 3, "AF", 2, 30)
# dog_01.bark()
# dog_01.jump()
# dog_01.sleep()
# dog_01.run()
# dog_01.birthday()
# print(dog_01.age)
# dog_01.change_height()
# dog_01.change_weight(0.5)
# print(f"weight {dog_01.weight} height {dog_01.height}")
# dog_01.new_jump(0.3)
#
cat_01 = Cat("c", 2, "CF", 5, 20)
# cat_01.meow()
# cat_01.jump()
# cat_01.sleep()
# cat_01.run()
# cat_01.birthday()
# print(cat_01.age)
# cat_01.change_height()
# cat_01.change_weight(0.5)
# print(f"weight {cat_01.weight} height {cat_01.height}")
# cat_01.new_jump(4)
#
parrot_01 = Parrot("f", 25, "FF", 0.1, 10, "asd")
# parrot_01.fly()
# parrot_01.jump()
# parrot_01.sleep()
# parrot_01.run()
# parrot_01.birthday()
# print(parrot_01.age)
# parrot_01.change_height()
# parrot_01.change_weight(0.5)
# print(f"weight {parrot_01.weight} height {parrot_01.height}")
# parrot_01.fly()
# parrot_01.new_jump(4)
# print(parrot_01.species)

def animals_voices(*args):
    for i in args:
        i.voice()


animals_voices(dog_01, cat_01, parrot_01)