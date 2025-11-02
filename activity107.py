class fruit:
    taste = "sweet"
    def __init__(self, name, color):
        self.name = name
        self.color = color
god = fruit('Apple', 'Red')
banana = fruit('Banana', 'Yellow')
print(god.name)
print(banana.color)


class student:
    grade = 10
    print("Welcome to grade", grade)
ob = student
