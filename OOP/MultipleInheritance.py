class Father:
    def father_property(self):
        print("This is father's property.")
class Mother:
    def mother_property(self):
        print("This is mother's property.")
class Child(Father, Mother):
    def child_property(self):
        print("This is child's property.")
child = Child()
child.father_property()
child.mother_property()
child.child_property()
