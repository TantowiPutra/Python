from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        self.num_eyes = 2

    @abstractmethod
    def breathe(self):
        pass


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def breathe(self):
        print("Blub blub blub..")


nemo = Fish()

nemo.swim()
nemo.breathe()
