student = {
    "name": "Vyshnavi",
    "course": "CSD",
    "year": 2
}
swapped = {}
for key, value in student.items():
    swapped[key] = str(value)
print("Original Dictionary:")
print(student)
print("\nValues Converted to Strings:")
print(swapped)
