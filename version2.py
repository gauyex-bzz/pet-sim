import random


class Pet:
    def __init__(self, name, animal):
        self._name = name
        self._animal = animal
        self._feed = 3
        self._friendship = 0

    def friendship_up(self):
        self.friendship += 0.1

    def friendship_down(self):
        self.friendship -= 1

    def hungry(self):
        print(f'{self.name} is too hungry to do that. You should feed it.')

    def hunger(self):
        self.feed -= 1

    def feed_pet(self):
        print(f'{self.name} was fed.')
        amount = int(input('How much food would you like to give it? (1-3) \n'))
        self.friendship_up()
        self._feed += amount
        if self.feed >= 8:
            print(f'{self.name} is now fat. You should stop feeding it.')
        if self.feed >= 13:
            print(f'{self.name} is now obese. Please stop feeding that poor {self.animal}.')
        if self.feed >= 18:
            print(f'{self.name} is now dead. You killed it by overfeeding it. What a horrible death.')
            goodbye()

    def play(self):
        randint = random.randint(1, 1000)
        if self.feed < 1:
            self.hungry()
        else:
            if randint == 1:
                print(f'{self.name} broke its neck while playing. What the hell were you doing?.')
                goodbye()
            elif randint == 2:
                print(f'{self.name} was hit by a car while playing. Better watch out next time.')
                goodbye()
            else:
                print(f'{self.name} played with you.')
                self.friendship_up()
                self.feed -= 0.5

    def swim(self):
        drown = random.randint(1, 1000)
        if self.feed < 1:
            self.hungry()
        else:
            print(f'{self.name} swam.')
            if drown == 1:
                print(f'{self.name} drowned. You are a terrible pet owner.')
                exit()
            else:
                self.friendship_up()
                self.feed = self.feed - 0.5

    def sleep(self):
        if self.feed < 3:
            print(f'{self.name} is too hungry to sleep. You should feed it.')
        else:
            print(f'{self.name} slept.')
            self.friendship_up()
            self.feed = self.feed - 2

    def release(self):
        print(f'{self.name} was released. It is now free.')
        exit()

    def hit(self):
        print(f'You hit {self.name}. This is animal abuse. Shame on you.')
        self.friendship_down()
        self.hunger()
        if self.friendship < 0:
            print(f'{self.name} ran away because it got scared of you.')
            goodbye()
        elif self.feed < 1:
            print(f'{self.name} died becaue it was too weak. You killed your pet. Shame on you.')

    @property
    def name(self):
        return self._name

    @property
    def animal(self):
        return self._animal

    @property
    def feed(self):
        return self._feed

    @feed.setter
    def feed(self, value):
        self._feed = value

    @property
    def friendship(self):
        return self._friendship

    @friendship.setter
    def friendship(self, value):
        self._friendship = value

    def __str__(self):
        return f'\nName: {self.name}\n' \
               f'Animal: {self.animal}\n' \
               f'Feed: {self.feed}\n' \
               f'Friendship: {self.friendship}\n'


def select_pet(list):
    if not list:
        print('No pets available.')
        return None


def goodbye():
    print('\n##### Goodbye! #####')
    exit()


def pet_menu(pet):
    print(pet)
    print('\tOptions: \n\tFeed, Play, Swim, Sleep, Release, Hit')
    choice = input('What would you like to do? \n')
    if choice == 'feed':
        pet.feed_pet()
    elif choice == 'play':
        pet.play()
    elif choice == 'swim':
        pet.swim()
    elif choice == 'sleep':
        pet.sleep()
    elif choice == 'release':
        pet.release()
    elif choice == 'hit':
        pet.hit()
    else:
        print('Invalid choice.')


if __name__ == '__main__':
    pets = [Pet('George', 'Monkey')]
    print('##### Welcome to pet simulator! #####\n')
    while True:
        pet_menu(pets[0])
