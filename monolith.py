

planet = 'Arriving at Earth...'

print(
    '''welcome to the solar system!
    There are 9 planets to explore
    '''
    )

name = input('what is your name?')


print('Nice to meet you ' + name)

print(
    '''My name is a Jenkins, I'm a AI here to guide you!
    Let's go on a adventure!
    '''
    )

choice = input('Shall I randomly choose a planet for you to visit? (Y or N)')
print(choice)
#option for selecting a planet

if choice == 'Y' or 'yes' or 'Yes':
    print(planet)
elif choice == 'N' or 'No' or 'no':
    planet_input = input('Please type the name of the planet you want to visit')
    print(planet_input)
    if choice != '':
        print(planet)
    else:
        print('no input detected, try again')
else:
    print("improper output")
#text input here


