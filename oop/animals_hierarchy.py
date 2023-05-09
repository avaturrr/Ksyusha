"""Создать файл animals_hierarchy.py. Реализовать следующую структуру:
oop_27
Реализовать интерфейсы: Feline(), Canine().
Все кошачьи должны уметь царапаться. Все собачьи должны уметь выть на луну.
"""
from abc import ABC, abstractmethod


class Animal:
    pass


class Feline(ABC):
    @abstractmethod
    def scratch(self):
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def howl(self):
        raise NotImplementedError


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class Cat(Pet, Feline):
    def scratch(self):
        print("scratch-scratch")


class Dog(Pet, Canine):
    def howl(self):
        print("howl at the moon")


class Lion(WildAnimal, Feline):
    def scratch(self):
        print("scratch-scratch")


class Wolf(WildAnimal, Canine):
    def howl(self):
        print("howl at the moon")


def main():
    lion_alex = Lion()
    lion_alex.scratch()


if __name__ == "__main__":
    main()
