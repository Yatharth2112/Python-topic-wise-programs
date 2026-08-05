class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter number: "))
    if num<0:
        raise NegativeNumberError("Number cannot be negative")
    result = 45/num
    print(f"The result is {result}")

except ValueError:
    print("Enter a number")

except ZeroDivisionError:
    print("Cannot divide by Zero")

except NegativeNumberError as e:
    print(f"Error: {e}")
