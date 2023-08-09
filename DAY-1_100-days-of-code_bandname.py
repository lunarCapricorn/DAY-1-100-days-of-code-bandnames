class NameGenerator:
    def __init__(self, name, cityName, petName):
        self.name = name
        self.resultingName = cityName + ' ' + petName

    def howManyNames(self):
        print(f"Here are all the names, in total there are {len(objs)} unique names.")
        for name in  objs:
            print(name)

    def bandName(self):
        print(f'Haza, your new band name, enjoy: {self.resultingName}')

def responsesToUser(argument):
    switcher = {
        'repeat_yes' : 'Very well.',
        'repeat_no' : 'Thank you and take care. :).',
        'show_yes' : 'Of course.',
        'show_no' : 'No issues.',
    }

    return switcher.get(argument)

print("\n---   ---   ---   ---   ---   ---")
print('Hello and welcome.\nThis is a piece of software designed to generate you a band name. Tell me:')
i = True
objs = {}
numb = 1
while i: # stores user input in a dictionary and displays current band name
    name = 'Bandname {}'.format(numb)
    cityName = input('What is your childhood city?\n')
    petName = input('What is/was your pets name?\n')
    printingStuff = NameGenerator('', cityName, petName)
    objs[name, printingStuff.resultingName] = name, printingStuff.resultingName

    numb += 1
    repeat = True
    printingStuff.bandName()
    # Options for user, can display all band names, afterward, user can choose to add more or quit the program
    while repeat:
        argument = 'show_' + input('Would you like to see all the names generated? [yes/no] ')
        if (argument == 'show_yes'):
            printingStuff.howManyNames()

        if (argument == 'show_no'):
            argument = 'repeat_' + input('Continue? [yes/no] ')

            print(responsesToUser(argument))
            if (argument == 'repeat_no'):
                exit()
            elif (argument != 'repeat_no' and argument != 'repeat_yes'):
                print('For now, we only support words "yes" and "no". Please try again.')
            else: 
                repeat = False
        elif (argument != 'show_no' and argument != 'show_yes'):
                print('For now, we only support words "yes" and "no". Please try again.')