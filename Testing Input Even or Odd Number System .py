#test input value try-except
while True:
    try:
        number = int(input("enter a number: "))
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
        break
    except:
        print("Invalid value, try again")
