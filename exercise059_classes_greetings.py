# Napisz klasę Person, która:
# w konstruktorze (__init__) przyjmuje imię i wiek,
# zapisuje je jako atrybuty,
# ma metodę greet(), która zwraca napis:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

person1 = Person("Alice", 30)
print(person1.greet())