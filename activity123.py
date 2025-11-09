class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "point({0}, {1})".format(self.y, self.x)
p1 = point(2, 7)
print(p1)