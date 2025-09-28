try:
    number = float(input("Enter a number: "))
    print(" The number is:", number )
except ValueError as ex:
    print("Error details:", ex)
       
