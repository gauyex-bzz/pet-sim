import time

animal = input('Please choose one of the following pets: cat, dog, rabbit or hamster.\n')

while animal not in ['cat', 'dog', 'rabbit', 'hamster']:
    animal = input('This animal is not available at the pet store. Please choose one of the following: cat, dog, '
                   'rabbit, hamster. \n')
    exit()

name = input(f'Please enter a name for your {animal}\n')
keep = input(f'Congrats! You now own a {animal} named {name}! Would you like to keep it? (yes/no)\n')

friendshipLevel = 0

if keep == 'yes':
    print(f'Great! You can now interact with {name}! Your friendship level is {friendshipLevel}.')
else:
    print(f'{name} was released.')
    exit()

while keep:
    interact = input(f'Would you like to interact with {name}? (yes/no)\n')
    while interact == 'no':
        time.sleep(5)
        interact = input(f'Would you like to interact with {name} now? (yes/no)\n')
        if interact == 'yes':
            break
    interactionType = input(f'What would you like to do with {name}? (feed, play, swim, sleep, release, sell, kill)\n')
    if interactionType == 'feed':
        print(f'{name} was fed.')
        friendshipLevel += 0.2
    elif interactionType == 'play':
        print(f'{name} played with you.')
        friendshipLevel += 0.1
    elif interactionType == 'swim':
        print(f'{name} swam.')
        friendshipLevel += 0.1
    elif interactionType == 'sleep':
        print(f'{name} slept.')
        friendshipLevel += 0.1
    elif interactionType == 'release':
        print(f'{name} was released. You can choose another pet by restarting the game.')
        exit()
    elif interactionType == 'sell':
        print(f'{name} was sold for $3. Feel happy now?')
        exit()
    elif interactionType == 'kill':
        print(f'{name} was killed. I hope you feel bad.')
        exit()
