

name = ''
planet_to_visit = ''
choice = ''

def introduction():
    print(
    '''welcome to the solar system!
    There are 9 planets to explore
    ''')

def explanation():
    print(
    '''My name is a Jenkins, I'm a AI here to guide you!
    Let's go on a adventure!
    ''')

def earth():
    print('Arriving at Earth')

def input_name():
    print('What is your name?')
    name = input('')

def random_planet():
    global choice
    print('Shall I randomly choose a planet for you to visit? (Y or N)')
    choice = input('')
    if choice == 'Y' or 'yes' or 'Yes':
        earth()
    elif choice == 'N' or 'No' or 'no':
        planet_input = input('Please type the name of the planet you want to visit')
        input_planet()
        if planet_to_visit!= '':
            earth()
        else:
            print('no input detected, try again')
    else:
        print("improper output")


def input_planet():
    global planet_to_visit 
    print('Please type the name of the planet you want to visit')
    planet_to_visit = input('')

#main function
introduction()
input_name()
explanation()
random_planet()
