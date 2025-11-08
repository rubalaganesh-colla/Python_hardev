class Vehicle:
    def __init__(self, name, seating_capacity, fare_per_person):
        self.name = name
        self.seating_capacity = seating_capacity
        self.fare_per_person = fare_per_person

    def total_fare(self):
        return self.seating_capacity * self.fare_per_person


class Bus(Vehicle):
    def total_fare(self):
        base_fare = super().total_fare()
        maintenance_charge = base_fare * 0.2  # 20% maintenance charge
        return base_fare + maintenance_charge


# Example usage
if __name__ == "__main__":
    bus = Bus("City Bus", 50, 100)  # 50 seats, fare per person is 100
    print(f"Total fare for {bus.name}: ₹{bus.total_fare()}")
