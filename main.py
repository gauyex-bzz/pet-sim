animal = input('Please choose one of the following pets: cat, dog, rabbit or hamster.\n')

while animal not in ['cat', 'dog', 'rabbit', 'hamster']:
    animal = input('This animal is not available at the pet store. Please choose one of the following: cat, dog, '
                   'rabbit, hamster. \n')
    exit()

name = input(f'Please enter a name for your {animal}\n')
keep = input(f'Congrats! You now own a {animal} named {name}! Would you like to keep it? (yes/no)\n')

if keep == 'yes':
    print(f'Great! You can now interact with {name}!')
else:
    print(f'{name} was released.')
