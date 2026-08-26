student = {
    "name": "Vyshnavi",
    "course": "CSD",
    "year": 2
}
inverted = {}
for key, value in student.items():
    inverted[value] = key
print("Original Dictionary:")
print(student)
print("\nInverted Dictionary:")
print(inverted)
