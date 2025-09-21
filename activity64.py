def cube_of_cube(n):
    value = (n ** 3)
    return value
def by_three(number):
    if number % 3 == 0:
        return cube_of_cube(number)
    else:
        return False
print(by_three(3))
print(by_three(4))