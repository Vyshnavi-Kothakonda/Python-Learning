try:
    number = int(input("Enter a number: "))
    try:
        result = 100 / number
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
