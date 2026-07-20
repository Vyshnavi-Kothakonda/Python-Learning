class Student:
    school = "SWEC"
    @classmethod
    def show_school(cls):
        print("School:", cls.school)
Student.show_school()
