class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Valid age:", age)


while True:
    try:
        age = int(input("Enter age (-1 to quit): "))

        if age == -1:
            print("Program Ended.")
            break

        check_age(age)

    except InvalidAgeError as e:
        print("Custom Error:", e)

        with open("error_log.txt", "a") as file:
            file.write(str(e) + "\n")

    except ValueError:
        print("Please enter numbers only.")