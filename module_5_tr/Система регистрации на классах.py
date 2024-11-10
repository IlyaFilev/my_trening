class Database:

    def __init__(self):
        self.data = {}    # Словарик с данными: Имя + пароль

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password




if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую, выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if len(password) < 8 or password.islower() == True or any(map(str.isdigit, password)) == False:
                print('password должен содержать не менее 8 символов, хотя бы 1 цифру и хотя бы 1 заглавную букву')
                continue
            elif password != password2:
                print("не совпадение паролей, попробуйте ещё раз")
                continue
            database.add_user(user.username, user.password) # формирование словаря
            print(database.data)


