try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Enter + for addition \nEnter - for subraction \nEnter * for multiplication \nEnter / for Division")
    c = input("Enter your Choice: ")

    match c:
        case "+":
            print(f"The result is: {a+b}")

        case "-":
            print(f"The result is: {a-b}")

        case "*":
            print(f"The result is: {a*b}")

        case "/":
            print(f"The result is: {a/b}")           
        

except Exception as e:
    print("Enter a valid value of A and B")