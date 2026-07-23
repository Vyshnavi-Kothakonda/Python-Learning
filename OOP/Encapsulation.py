class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
student = Student("Vyshnavi", 19)
print("Name:", student.get_name())
print("Age:", student.get_age())
