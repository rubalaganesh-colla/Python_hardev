class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("Blu", 10)
woo = parrot("Woo", 15)
print("blu is a {}".format(blu.name))
print("woo is {} years old".format(woo.age))
print("{}is {} years old".format(blu.name, blu.age))
print("{}is {} years old".format(woo.name, woo.age))
