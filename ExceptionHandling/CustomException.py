class AgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above.")
    print("Eligible.")
try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeError as e:
    print("Error:", e)
