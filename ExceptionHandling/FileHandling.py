try:
    with open("data.txt", "w") as file:
        file.write("Welcome to Python File Handling!")
    print("Data written successfully.")
    with open("data.txt", "r") as file:
        content = file.read()
    print("File Content:")
    print(content)
except IOError as e:
    print("File Error:", e)
