# Match Case Statement

day = int(input("Enter day (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")