filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found.")
