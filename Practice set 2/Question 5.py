first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
choice = int(input("Enter 1 to add\nEnter 2 to subtract\nEnter 3 to multiply\nEnter 4 to divide\nEnter your choice: "))
match choice:
    case 1:
        print("The addition is ", first + second)
    case 2:
        print("The subtraction is ", first - second) 
    case 3:
        print("The multiplication is ", first * second) 
    case 4:
        print("The division is ", first / second)
    case _:
        print("Invalid choice.")
                      