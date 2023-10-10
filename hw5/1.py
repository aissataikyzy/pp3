import re

#db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}

def show_db():
    with open ('db.txt', 'r') as file:
        all = file.read()
        print(all)


def change_name(old_name, new_name, password):
    # Создаем словарь для хранения данных из файла
    db = {}
    
    # Читаем данные из файла и заполняем словарь
    with open('db.txt', 'r') as file:
        for line in file:
            name, stored_password = line.strip().split(':')
            db[name] = stored_password
    
    # Проверяем пароль
    while password != db.get(old_name):
        password = input('Wrong password! Try again: ')

    # Меняем имя и перезаписываем файл
    if old_name in db:
        db[new_name] = db.pop(old_name)
        with open('db.txt', 'w') as file:
            for name, stored_password in db.items():
                file.write(f'{name}:{stored_password}\n')


def check_password(password):
    while not (re.search(r'[A-Z]', password) and
               re.search(r'[a-z]', password) and
               re.search(r'[@#$%^&*]', password) and
               re.search(r'\d', password) and
               len(password) >= 6):
        password = input('Enter another password: ')

    return True



def change_password(username, new_password, current_password):
    db = {}
    
    with open('db.txt', 'r') as file:
        for line in file:
            name, stored_password = line.strip().split(':')
            db[name] = stored_password

    while current_password != db.get(username):
        current_password = input('Wrong password! Try again: ')

    if username in db:
        db[username] = new_password
        if check_password(new_password) == True:
            with open('db.txt', 'w') as file:
                for name, stored_password in db.items():
                    file.write(f'{name}:{stored_password}\n')
            print('Password updated successfully.')
        

def add_user(name, password):
    db = {}
    with open('db.txt', 'r') as file:
        for line in file:
            name, stored_password = line.strip().split(':')
            db[name] = stored_password

    while name in db.keys():
        name = input('Please choose another name: ')

    if check_password(password):
        db[name] = password
        with open('db.txt', 'w') as file:
            for name, stored_password in db.items():
                file.write(f'{name}:{stored_password}\n')
                print(f'User {name} added successfully!')
        


print("Welcome to the users database!")

while True:
    action = input("What would you like to do? (show db/add user/change name/change password/quit): ")
    
    if action == 'show db':
        show_db()
    elif action == 'add user':
        name = input('Enter name: ')
        password = input('Enter password: ')
        add_user(name, password)
    elif action == 'change name':
        old_name = input('Enter old name: ')
        new_name = input('Enter new name: ')
        password = input('Enter password: ')
        change_name(old_name, new_name, password)
    elif action == 'change password':
        username = input('Enter your name: ')
        new_password = input('Enter new password: ')
        current_password = input('Enter current password: ')
        change_password(username, new_password, current_password)
    elif action == 'quit':
        break  # Выход из цикла
    else:
        print("Invalid action. Please choose from 'show db', 'add user', 'change name', 'change password', or 'quit'.")
