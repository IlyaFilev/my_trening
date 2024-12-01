'''Создание функций на лету'''
from shutil import which

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
res_list = list(map(lambda x, y: x == y, first, second)) # map: x[0]==y[0], x[1]==y[1], и далее по позициям
print(res_list)

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{str(i)}\n')  # данные любого типа конверт-м в строки и добавляем переход на след. стр.

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 235, 546, {'a': 5, 'b': 2})

# Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        word = choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
