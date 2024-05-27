
users = {'admin': hash('pass')}

nickname = 'admin'
password = 'pass'

def registration(nickname, password):
    if users.get(nickname):
        print('Пользователь существует!')
    else:
        users[nickname] = hash(password)

registration(nickname, password)

print(users)