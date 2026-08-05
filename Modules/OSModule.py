import os
print("Current Working Directory:")
print(os.getcwd())
print("\nFiles and Folders:")
for item in os.listdir():
    print(item)
