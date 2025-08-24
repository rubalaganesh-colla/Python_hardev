print("enter a number (numerater):")
numerater=int(input())
print("enter a number (denominator):")
denominator=int(input())

if numerater%denominator==0:
    print("\n" +str(numerater) + " is completely divisible by " + str(denominator))
else:
    print("\n" +str(numerater) + " is not completely divisible by " + str(denominator))
