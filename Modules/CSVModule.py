import csv
students = [
    ["Name", "Age", "Course"],
    ["Vyshnavi", 19, "CSD"],
    ["Anjali", 20, "CSE"],
    ["Rahul", 19, "ECE"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("CSV file created successfully.")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("\nStudent Details:")
    for row in reader:
        print(row)
