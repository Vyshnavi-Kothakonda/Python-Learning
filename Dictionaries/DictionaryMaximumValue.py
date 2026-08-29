marks = {
    "math": 85,
    "science": 92,
    "english": 78,
    "computer": 95
}
highest_subject = max(marks, key=marks.get)
print("Highest Marks:", marks[highest_subject])
print("Subject:", highest_subject)
