def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("Select operation.")
choice= int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == 1:
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == 2:
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == 3:
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == 4:
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
    
    