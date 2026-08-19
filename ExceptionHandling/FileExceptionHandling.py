try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program execution completed.")
