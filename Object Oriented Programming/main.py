class User:
    def __init__(self, id, username):
        self.id       = id
        self.username = username

    def get_user_detail(self):
        print(f"Id: {self.id}, Username: {self.username}")
        return

user_1 = User("001", "Tantowi")
user_1.id       = "001"
user_1.username = "Tantowi"

user_2 = User("002", "Tantowi")
user_2.id = "002"
user_2.username = "Jack"

user_1.get_user_detail()

# INHERITANCE
class Animal:
    def speak(self):
        print("Some Sound")

class Dog(Animal):
    def speak(self): # Method speak disini Override Parent Class
        print("Woof!")

new_dog = Dog()
new_dog.speak()

# ABSTRACT / INTERFACE (CONTRACT)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 *10 * 10

new_circle = Circle()
print(new_circle.area())