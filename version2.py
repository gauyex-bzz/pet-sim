import random


class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
        self.feed = 3
        self.friendship = 0

    def friendship_up(self):
        self.friendship += 0.1

    def hungry(self, interaction):
        print(f'{self.name} is too hungry to {interaction}. You should feed it.')

    def interaction(self, interaction_type):
        if interaction_type == 'feed':
            amount = int(input(f'How much would you like to feed {self.name}? (1-3)\n'))
            print(f'{self.name} was fed.')
            self.friendship_up()
            self.feed += amount
            if self.feed == 8:
                print(f'{self.name} is now fat. You should stop feeding it.')
            if self.feed == 13:
                print(f'{self.name} is now obese. Please stop feeding that poor {self.animal}.')
            if self.feed == 18:
                print(f'{self.name} is now dead. You killed it by overfeeding it. What a horrible death.')
                exit()

        elif interaction_type == 'play':
            breakNeck = random.randint(1, 1000)
            if self.feed < 1:
                self.hungry(interaction_type)
            else:
                if breakNeck == 1:
                    print(f'{self.name} broke its neck while playing. You are a terrible pet owner.')
                    exit()
                else:
                    print(f'{self.name} played with you.')
                    self.friendship_up()
                    self.feed -= 0.5

        elif interaction_type == 'swim':
            drown = random.randint(1, 1000)
            if self.feed < 1:
                self.hungry(interaction_type)
            else:
                print(f'{self.name} swam.')
                if drown == 1:
                    print(f'{self.name} drowned. You are a terrible pet owner.')
                    exit()
                self.friendship_up()
                self.feed = self.feed - 0.5

        elif interaction_type == 'sleep':
            if self.feed < 2:
                print(f'{self.name} is too hungry to sleep. You should feed it.')
            else:
                print(f'{self.name} slept.')
                self.friendship_up()
                self.feed = self.feed - 2

        elif interaction_type == 'release':
            print(f'{self.name} was released. You can choose another pet by restarting the game.')
            exit()

        elif interaction_type == 'sell':
            print(f'{self.name} was sold for $3. Feel happy now?')
            exit()

        elif interaction_type == 'hit':
            print(f'{self.name} was hit.')
            self.friendship -= 1
            if self.friendship < 0:
                print(f'{self.name} ran away because it got scared of you. You are a monster.')
                exit()

        if self.feed < 0:
            print(f'{self.name} starved to death. You are a terrible pet owner.')
            exit()
