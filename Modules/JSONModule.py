import json
student = {
    "name": "Vyshnavi",
    "age": 19,
    "course": "CSD"
}
json_data = json.dumps(student, indent=4)
print("JSON Data:")
print(json_data)
data = json.loads(json_data)
print("\nStudent Name:", data["name"])
print("Course:", data["course"])
