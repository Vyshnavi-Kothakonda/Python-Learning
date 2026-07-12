text = input("Enter text to append: ")
with open("output.txt", "a") as file:
    file.write(text + "\n")
print("Text appended successfully.")
