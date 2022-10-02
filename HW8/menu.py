from controller import *

def start():
    print('\nWelcome to the school information system!')

    menu1 = '\nChoose command:\n1 - print list of tables\n2 - add line to table\n0 - exit\n\nYour choice: '
    count = 0
    choice = int(input(menu1))

    while choice != 0:
            if choice == 1:
                print_all_tables()
                # choice = int(input(menu1))
                menu2 = '\nChoose command:\n1 - print schedule table\n2 - print teachers table\n0 - exit to previous menu\n\nYour choice: '
                choice2 = int(input(menu2))
                while choice2 != 0:
                    if choice2 == 1:
                        sql_print_schedule()
                        choice2 = int(input(menu2))
                    elif choice2 == 2:
                        sql_print_teachers()
                        choice2 = int(input(menu2))
                choice = int(input(menu1))
            elif choice == 2:
                choice1 = int(input('\nChoose table:\n1 - schedule\n2 - teachers\n\nYour choice: '))
                if choice1 == 1:
                    sql_print_schedule()
                    sql_insert_line_to_schedule()
                    print()
                    sql_print_schedule()
                elif choice1 == 2:
                    sql_print_teachers()
                    sql_insert_line_to_teachers()
                    print()
                    sql_print_teachers()
                else:
                    print('Incorrect input!\n')
                choice = int(input(menu1))
            else:
                print('Incorrect input!\n')
                choice = int(input(menu1))
