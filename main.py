import time

animal = input('Please choose one of the following pets: cat, dog, rabbit or hamster.\n')

while animal not in ['cat', 'dog', 'rabbit', 'hamster']:
    animal = input('This animal is not available at the pet store. Please choose one of the following: cat, dog, '
                   'rabbit, hamster. \n')
    exit()

name = input(f'Please enter a name for your {animal}\n')
keep = input(f'Congrats! You now own a {animal} named {name}! Would you like to keep it? (yes/no)\n')

friendshipLevel = 9.9
feed = 0

if keep == 'yes':
    print(f'Great! You can now interact with {name}! Your friendship level is {friendshipLevel}.')
else:
    print(f'{name} was released.')
    exit()


def hungry():
    print(f'{name} is hungry and does not want to {interactionType}. You should feed it.')


def friendship_up():
    global friendshipLevel
    if friendshipLevel < 10:
        friendshipLevel += 0.1


while keep:
    if friendshipLevel in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f'Congrats! Your friendship level is now {friendshipLevel}.')
    if friendshipLevel == 10:
        print(f'You have reached the maximum friendship level with {name}!')
    interact = input(f'\nWould you like to interact with {name}? (yes/no)\n')
    while interact == 'no':
        time.sleep(5)
        interact = input(f'\nWould you like to interact with {name} now? (yes/no)\n')
        if interact == 'yes':
            break
    interactionType = input(f'What would you like to do with {name}? (feed, play, swim, sleep, release, sell, kill, '
                            f'slap)\n')
    if interactionType == 'feed':
        print(f'{name} was fed.')
        friendship_up()
        feed += 1
        if feed == 5:
            print(f'{name} is now fat. You should stop feeding it.')
        if feed == 10:
            print(f'{name} is now obese. Please stop feeding that poor {animal}.')
        if feed == 15:
            print(f'{name} is now dead. You killed it by overfeeding it. What a horrible death.')
            exit()
    elif interactionType == 'play':
        if feed < 1:
            hungry()
        else:
            print(f'{name} played with you.')
            friendship_up()
    elif interactionType == 'swim':
        if feed < 1:
            hungry()
        else:
            print(f'{name} swam.')
            friendship_up()
    elif interactionType == 'sleep':
        print(f'{name} slept.')
        friendship_up()
        feed = 2
    elif interactionType == 'release':
        print(f'{name} was released. You can choose another pet by restarting the game.')
        exit()
    elif interactionType == 'sell':
        print(f'{name} was sold for $3. Feel happy now?')
        exit()
    elif interactionType == 'kill':
        print(f'{name} was killed. I hope you feel bad.')
        exit()
    elif interactionType == 'slap':
        print(f'{name} was slapped. You are a horrible person.')
        friendshipLevel -= 0.3
        if friendshipLevel < 0:
            print(f'{name} ran away because it got scared of you. You are a monster.')
            exit()
