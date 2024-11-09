class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50

    def eat(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} поїла. Голод: {self.hunger}")

    def __str__(self):
        return f"{self.name} ({self.species})"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} додано до зоопарку.")

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def show_animals(self):
        print("Тварини у зоопарку:")
        for animal in self.animals:
            print(animal)


# Створення зоопарку та тварин
my_zoo = Zoo()
lion = Animal("Лев", "Хижак")
elephant = Animal("Слон", "Травоїдний")

# Додавання тварин до зоопарку
my_zoo.add_animal(lion)
my_zoo.add_animal(elephant)

# Показ тварин у зоопарку
my_zoo.show_animals()

# Годування всіх тварин у зоопарку
my_zoo.feed_all()
