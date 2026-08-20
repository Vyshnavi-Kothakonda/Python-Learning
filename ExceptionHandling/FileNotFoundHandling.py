try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("Error: data.txt was not found.")
