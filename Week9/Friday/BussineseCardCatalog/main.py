from utils import *


def main():
    create_table()
    print('Hello! This is your business card catalog. What would you like?(enter "help" to list all avaliable options')
    while True:
        choice = input('Your command: ')
        choice = choice.lower()
        if choice == 'add':
            add()
        elif choice == 'list':
            list()
        elif choice == 'delete':
            delete()
        elif choice == 'get':
            get()
        elif choice == 'help':
            help()
        elif choice == 'exit':
            break
        else:
            print('Invalid command! Please try again')


if __name__ == '__main__':
    main()