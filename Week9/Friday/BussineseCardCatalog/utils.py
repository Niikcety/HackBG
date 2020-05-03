import sqlite3


def create_table():
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS User(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        full_name VARCHAR(32) NOT NULL UNIQUE,
        email VARCHAR(48) NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        phone VARCHAR(15) NOT NULL,
        additional_info TEXT
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add():
    full_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter additional info (optional): ')
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO User(full_name, email, age, phone, additional_info)
      VALUES(?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (full_name, email, age, phone, additional_info))
    connection.commit()
    connection.close()


def list():
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    query = '''
    SELECT *
    FROM User
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print('ID: {}, Email: {}, Full name: {} \n'.format(row[0], row[2], row[1]))

    connection.commit()
    connection.close()


def get():
    id = input('Enter id: ')
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    query = f'''
    SELECT *
    FROM User
    WHERE id = {id}
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    print_helper(data)

    connection.commit()
    connection.close()


def delete():
    id = input('Enter id: ')
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    query = f'''
    SELECT *
    FROM User
    WHERE id = {id}
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    query = f'''
    DELETE FROM User
    WHERE id = {id}
    '''
    cursor.execute(query)
    if data == []:
        print('There is no business card associated with that id: {}'.format(id))
    else:
        print('Following contact is deleted successfully:')
        print_helper(data)
    connection.commit()
    connection.close()


def print_helper(data):
    try:
        print(16 * '#')
        print('ID: {}'.format(data[0][0]))
        print('Full name: {} '.format(data[0][1]))
        print('Email: {}'.format(data[0][2]))
        print('Age: {}'.format(data[0][3]))
        print('Phone: {}'.format(data[0][4]))
        print('Additional info: {}'.format(data[0][5]))
        print(16 * '#')
    except IndexError:
        print('There is no business card associated with this id')


def help():
    print('1. \'add\' - insert new business card')
    print('2. \'list\' - list all business cards')
    print('3. \'delete\' - delete a certain business card(\'ID\' is required)')
    print('4. \'get\' - display full information for a certain business card(\'ID\' is required)')
    print('5. \'help\' - list all avaliable options')
    print('6. \'exit\' - exit the program')
