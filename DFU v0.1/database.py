import sqlite3,random,hashlib,time

conn = sqlite3.connect('userdata.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, firstname TEXT, lastname TEXT, username TEXT, password TEXT)')

def credits():
    print('Creator: Leon Davis')

def newUser():
    firstname = input('First Name: ')
    lastname = input('Last Name: ')
    username = input('New Username: ')
    password = input('New Password: ')
    conpassword = input('Confirm Password: ')

    try:
        if password == conpassword:
            id = random.randrange(0,100000)
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            c.execute('SELECT id FROM users')

            for row in c.fetchall():
                if row == id:
                    id = random.randrange(0,100000)

            c.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?)',
                      (id, firstname, lastname, username, password))
            conn.commit()

        else:
            print('Passwords Don\'t Match')

    except:
        print('An Error Has Occured!')

def findUser():
    choice = input('Filter By (id, first name, last name, username): ')

    try:
        if choice.lower() == 'id':
            id = input('Find With ID: ')
            c.execute('SELECT * FROM users WHERE id=?',
                      (id,))

            for row in c.fetchall():
                print(row)

        elif choice.lower() == 'first name':
            firstname = input('Find With First name:')
            c.execute('SELECT * FROM users WHERE firstname=?',
                      (firstname,))

            for row in c.fetchall():
                print(row)

        elif choice.lower() == 'last name':
            lastname = input('Find With Last name:')
            c.execute('SELECT * FROM users WHERE lastname=?',
                      (lastname,))

            for row in c.fetchall():
                print(row)

        elif choice.lower() == 'username':
            username = input('Find With Username name:')
            c.execute('SELECT * FROM users WHERE username=?',
                      (username,))

            for row in c.fetchall():
                print(row)

        else:
            print('Choice Invalid!')

    except:
        print('An Error Has Occured!')

def updateUser():
    id = input('Users ID: ')
    choice = input('To Update (order is First Name, Last Name, Username. put 0 to change nothing): ')
    choice = choice.split(' ')
    firstname = choice[0]
    lastname = choice[1]
    username = choice[2]

    try:
        c.execute('SELECT * FROM users')

        for row in c.fetchall():
            if choice[0] == 0:
                firstname = c.execute('SELECT firstname FROM users')

            if choice[1] == 0:
                lastname = c.execute('SELECT lastname FROM users')

            if choice[2] == 0:
                username = c.execute('SELECT username FROM users')

            c.execute('UPDATE users SET firstname=?, lastname=?, username=? WHERE id=?',
                      (firstname,lastname,username,id))
            conn.commit()

    except:
        print('An Error Has Occured!')

def deleteUser():
    id = input('Users ID: ')

    try:
        if id == 'all':
            c.execute('DELETE FROM users')
            conn.commit()

        else:
            c.execute('DELETE FROM users WHERE id=?',
                      (id,))
            conn.commit()

    except:
        print('An Error Has Occured!')

def addusersFromList():
    filename = input('File Name (remember to place it in this files location): ')
    filename += '.txt'
    num = 0
    
    with open(filename, 'r') as file:
        file = file.read().split('\n')

        try:
            for words in file:
                words = words.split(' ')

                firstname = words[0]
                lastname = words[1]
                username = words[2]
                password = words[3]
                password = hashlib.sha256(password.encode('utf-8')).hexdigest()

                id = random.randrange(0, 100000)
                c.execute('SELECT id FROM users')

                for row in c.fetchall():
                    if row == id:
                        id = random.randrange(0, 100000)

                num += 1
                print(num)

                c.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?)',
                          (id, firstname, lastname, username, password))
                conn.commit()

        except:
            print('Done!')

def connClose():
    conn.close()

################################################################################################
    
def commands():
    print('\n')
    choice = input('Command (type help to see options): ')

    try:
        if choice.lower() == 'help':
            print('Commands:')
            print('help - for list of commands')
            print('nu - to create new user')
            print('lu - to find user by listed options')
            print('du - to delete user')
            print('uu - update users details order is explained')
            print('aff - add users from a .txt file')
            print('exit - to quit the application')
            commands()

        elif choice.lower() == 'nu':
            newUser()
            commands()

        elif choice.lower() == 'lu':
            findUser()
            commands()

        elif choice.lower() == 'du':
            deleteUser()
            commands()

        elif choice.lower() == 'uu':
            updateUser()
            commands()

        elif choice.lower() == 'aff':
            addusersFromList()
            commands()

        elif choice.lower() == 'exit':
            print('Goodbye!')
            connClose()
            time.sleep(2)
            exit()

        else:
            print('Invalid Commands!')
            commands()

    except:
        print('An Error Has Occured!')

commands()
