import commands
import json
import json_recorder

def start():
    print('\n Welcom to the phonebook!')

    menu1 = 'Choose command:\n 1 - print phonebook\n 2 - add a record to phonebook\n 0 - exit\n\n Your choice: '

    choice = int(input(menu1))

    while choice != 0:
        if choice == 2:
            dic = json_recorder.read_json()
            print('Enter first name, last name, phone number, description separated by space:\n')
            commands.add_record(dic)
            json_recorder.write_json(dic)
            choice = int(input(menu1))
        elif choice == 1:
            print('\n')
            dic = json_recorder.read_json()
            commands.print_phonebook(dic)
            print('\n')
            choice = int(input(menu1))
        else:
            print('\n Incorrect input!\n')
            choice = int(input(menu1))
