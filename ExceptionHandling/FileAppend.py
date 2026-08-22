try:
    with open("data.txt", "a") as file:
        file.write("\nLearning Python file handling.")
    print("Data appended successfully.")
    with open("data.txt", "r") as file:
        content = file.read()
    print("\nFile Content:")
    print(content)
except IOError as e:
    print("File Error:", e)
