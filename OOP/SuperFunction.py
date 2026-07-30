class Animal:
    def __init__(self):
        print("Animal constructor")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")
dog = Dog()
