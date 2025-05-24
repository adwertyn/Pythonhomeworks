class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Moo...")
        self.milk_production = milk_production

    def milk(self):
        print(f"{self.name} produced {self.milk_production} liters of milk today.")

class Chicken(Animal):
    def __init__(self, name, age, eggs_per_day):
        super().__init__(name, age, "Chipchip...")
        self.eggs_per_day = eggs_per_day

    def egg(self):
        print(f"{self.name} laid {self.eggs_per_day} eggs today.")

class Pig(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, "Xrxr...")
        self.weight = weight

    def mass(self):
        print(f"{self.name} (weighing {self.weight} kg) is walking in the garden")

masha = Cow("Masha", 5, 12)
chicky = Chicken("Chicky", 2, 3)
pigy = Pig("Pigy", 4, 120)

for animal in [masha, chicky, pigy]:
    animal.eat()
    animal.sleep()
    animal.make_sound()

masha.milk()
chicky.egg()
pigy.mass()
