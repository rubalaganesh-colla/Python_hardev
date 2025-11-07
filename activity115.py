class circle():
    def __init__(self,r):
        self.radius=r
    def circle_area(self):
        return 3.14*self.radius*self.radius
    def circle_perimeter(self):
        return 2*3.14*self.radius
    def circle_diameter(self):
        return 2*self.radius
    def circle_circumference(self):
        return 2*3.14*self.radius
newCircle = circle(7)
print(newCircle.circle_area())
print(newCircle.circle_perimeter())
print(newCircle.circle_diameter())
print(newCircle.circle_circumference())