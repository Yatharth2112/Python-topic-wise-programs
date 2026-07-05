def safe_divide(a, b):
    if b == 0:
        return 0 
    return a / b

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print("Answer: ", safe_divide(num1, num2))
