try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
    print("File Lines:")
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print("File not found.")
