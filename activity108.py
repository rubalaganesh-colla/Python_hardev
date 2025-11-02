class vechile:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

model = vechile("Audi", 300, 30)
print ("model max speed:", model.max_speed, "kmph")
print("model mileage:", model.mileage,"kmpl")