class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent class.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent class.")
class Child(Parent):
    def child_method(self):
        print("This is the child class.")
obj = Child()
obj.grandparent_method()
obj.parent_method()
obj.child_method()
