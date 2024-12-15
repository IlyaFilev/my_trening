'''
Очереди для обмена данными между потоками
Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
'''
import threading
import time
from queue import Queue
from random import randint

from pygame.mixer_music import queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    # def run (self):
    #     time.sleep(randint(1, 1)) # Обладать run, где происходит ожидание случайным образом от 3 до 10 с.


class Cafe:

    def __init__(self, *tables): # tables = [Table(number) for number in range(1, 6)]
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):  # Если есть свободный стол, то садить гостя за стол (назначать столу guest),
                # запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        for guest in guests:
            for table in self.tables:
                if table.guest is None: # Если есть свободный стол,
                    table.guest = guest # сажаем гостя за стол (назначать столу guest)
                    guest.start()       # и запускаем потока Гостя (обслуживание)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                else:
                    self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        '''Этот метод имитирует процесс обслуживания гостей.'''
        while not self.queue.empty():
            for table in self.tables:
                if table.guest and not table.guest.is_alive(): # если Поток Гостя не активен:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None # стол освободился

                if not self.queue.empty() and table.guest is None:
                    new_guest = self.queue.get()
                    table.guest = new_guest.name
                    print(f'{new_guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    new_guest.start()
                    break



'''Выполняемый код:
class Table:
...
class Guest:
...
class Cafe:
...'''
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

