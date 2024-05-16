import random


class Pet:
    def __init__(self, name, animal):
        # attribute have to be set by setter
        self._hunger: int = 5
        self._level = 0.0
        self._name = name
        self._type = animal

    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.hunger = self.hunger - 2
        if self.hunger < 0:
            self.die()
            return 1
        if self.hunger < 2:
            print(f"{self.name} is hungry. ({self.hunger})")
        return 0

    def play(self):
        print(f"{self.name} is playing.")
        self.hunger = self.hunger - 1
        if self.hunger < 0:
            return self.die()
        self.level = self.level + 0.5
        return 0

    def hit(self):
        print(f"{self.name} is hit.")
        self.level = self.level - 1.0
        if self.level < 0:
            return self.flee()
        return 0

    def swim(self):
        print(f"{self.name} is swimming.")
        self.hunger = self.hunger - 2
        chance = 1
        if self.hunger < 1:
            chance = 5

        if random.randint(0, 1000) == chance:
            return self.drown()
        if self.hunger < 0:
            return self.die()
        return 0

    def die(self):
        print(f"{self.name} died.")
        return 1

    def flee(self):
        print(f"{self.name} fled.")
        return 2

    def drown(self):
        print(f"{self.name} drowned.")
        return 3

    def feed(self, value):
        self.hunger = self.hunger + value
        print(f"{self.name} is eating.\nNew hunger: {self.hunger}")

    @property
    def name(self):
        return self._name

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        self._hunger = value

    @property
    def type(self):
        return self._type

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self._level = round(self._level, 2)

    def __str__(self):
        return f"\tName: {self.name}\n" \
            f"\tType: {self.type}\n" \
            f"\tFeed: {self.hunger}\n" \
            f"\tLevel: {self.level}\n"


def choose(list):
    if not pets:
        print("No pets available.")
        return None

    string = "Choose a pet by it's name: \n"
    for pet in list:
        string += f"\t{pet.name} ({pet.type})\n"
    print(string)
    name = input("Enter the name of the pet: ")
    while not find(list, name):
        print("Pet not found.")
        name = input("Enter the name of the pet: ")
    for pet in list:
        if pet.name == name:
            return pet


def find(list, name):
    for pet in list:
        if pet.name == name:
            return True
    return False


def add():
    name = input("Enter the name of the pet: ")
    animal = input("Enter the type of the pet: ")
    return Pet(name, animal)


def pet_action(pet):
    while True:
        action = input("Choose an action (help): ")
        if action == "help":
            print("Available actions: \n"
                  "\tsleep\n"
                  "\tplay\n"
                  "\thit\n"
                  "\tswim\n"
                  "\tfeed\n"
                  "\tstats\n"
                  "\texit\n")
        elif action == "sleep":
            if pet.sleep() != 0:
                return 1
        elif action == "play":
            if pet.play() != 0:
                return 1
        elif action == "hit":
            if pet.hit() != 0:
                return 1
        elif action == "swim":
            if pet.swim() != 0:
                return 1
        elif action == "feed":
            try:
                pet.feed(int(input("Enter the amount of food: ")))
            except ValueError:
                print("Invalid input.")
        elif action == "stats":
            print(pet)
        elif action == "exit":
            break


def start(list):
    while True:
        action = input("Choose an action (help): ")
        if action == "help":
            print("Available actions: \n"
                  "\tadd\n"
                  "\tchoose\n"
                  "\tlist\n"
                  "\texit\n")
        elif action == "add":
            list.append(add())
        elif action == "choose":
            pet = choose(list)
            if pet:
                if pet_action(pet) != 0:
                    list.remove(pet)
        elif action == "list":
            for pet in list:
                print("\t" + pet.name + " (" + pet.type + ")" + "\n")
            if not list:
                print("No pets available.")
        elif action == "exit":
            break


if __name__ == '__main__':
    pets = [Pet("Xavier", "Slave")]  # in case you want some default pets, add them here
    print("##### Welcome to pet simulator! #####\n")
    start(pets)
    print("\n##### Goodbye! #####")