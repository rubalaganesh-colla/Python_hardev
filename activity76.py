valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        while number%5==0:
            print("bye")
        valid = True
    except ValueError as ex:
        print("Error details:", ex)