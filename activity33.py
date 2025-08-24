a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

avg=(a+b+c)/3
print("Average of three numbers is:",avg)

if avg>a and avg>b and avg>c:
    print("Average is greater than a,b and c")
elif avg>a and avg>b:
    print("Average is greater than a and b")
elif avg>a and avg>c:
    print("Average is greater than a and c")
elif avg>b and avg>c:
    print("Average is greater than b and c")
elif avg>a:
    print("Average is greater than a")
elif avg>b:
    print("Average is greater than b")
elif avg>c:
    print("Average is greater than c")
else:
    print("Average is not greater than a,b and c")
