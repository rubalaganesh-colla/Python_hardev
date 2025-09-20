a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
def area_of_rectangle(a, b):
    return a * b
def area_of_square(a):
    return a * a
print("Area of rectangle:", area_of_rectangle(a, b))
print("Area of square:", area_of_square(a))
