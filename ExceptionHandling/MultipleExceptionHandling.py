try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
