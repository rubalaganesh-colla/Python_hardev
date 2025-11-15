class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"
class Ferrari:
    def fuel_type(self):
        return "Petrol (High Octane)"
    def max_speed(self):
        return "350 km/h"
def car_details(car):
    try:
        print(f"Fuel Type: {car.fuel_type()}")
        print(f"Max Speed: {car.max_speed()}")
    except AttributeError:
        print("Error: The provided object does not have the required methods.")
if __name__ == "__main__":
    bmw_car = BMW()
    ferrari_car = Ferrari()
    print("BMW Details:")
    car_details(bmw_car) 
    car_details(ferrari_car)  