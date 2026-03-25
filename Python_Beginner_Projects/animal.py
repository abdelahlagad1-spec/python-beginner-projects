class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species.lower() == "dog":
            return "Woof!"
        elif self.species.lower() == "cat":
            return "Meow!"
        return "Unknown sound"

dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
