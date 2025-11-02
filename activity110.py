class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def display_details(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
    def set_name(self, name):
        self.name = name
    def set_breed(self, breed):
        self.breed = breed
    def set_age(self, age):
        self.age = age
    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def get_age(self):
        return self.age
if __name__ == "__main__":
    dog1 = Dog("Buddy", "Golden Retriever", 3)
    dog2 = Dog("Lucy", "Beagle", 5)
    print("Initial Dog Details:")
    dog1.display_details()
    dog2.display_details()
    dog1.set_name("Max")
    dog1.set_age(4)
    print("\nDog Details:")
    dog1.display_details()
