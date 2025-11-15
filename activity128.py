from abc import ABC, abstractmethod
class animal(ABC):
    def sound(self):
        pass
class human(animal):
    def move(self):
        print("Humans can walk and run")
class dog(animal):
    def bark(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("Cat meows")
h = human()
h.move()
d = dog()
d.bark()
c = cat()
c.sound()