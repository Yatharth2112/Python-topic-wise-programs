for i in range(1, 6):
    match i:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            pass
        case 4:
            print("Four")
        case 5:
            print("Five")
        case _:
            print("Number not in range 1-5")