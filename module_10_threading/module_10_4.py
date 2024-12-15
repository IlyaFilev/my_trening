'''
Очереди для обмена данными между потоками
Задача "Потоки гостей в кафе":
Три класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
и их обслуживания (discuss_guests).
'''
import threading
import time
from queue import Queue
from random import randint


class Table:
    def __init__(self, number: int):  # Объекты этого класса должны создаваться следующим способом - Table(1)
        self.number = number  # number - номер стола
        self.guest = None  # guest - гость, который сидит за этим столом (по умолчанию None)


class Guest(threading.Thread):  # Поток
    def __init__(self, name):
        threading.Thread.__init__(self)  # наследуется от Thread
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))  # Обладать run, где происходит ожидание случайным образом от 3 до 10 с.


class Cafe:

    def __init__(self, *tables):  # tables = [Table(number) for number in range(1, 6)]
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        '''Метод помещает гостя кафе за свободный стол (назначает столу guest) и запускает поток гостя
         и выводит на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".'''
        for guest in guests:
            table = self.table_free()  # Поиск свободного стола, через отдельную функцию, что бы не задваивать цикл
            if table:
                table.guest = guest  # сажаем гостя за свободный стол
                guest.start()  # и запускаем потока Гостя (обслуживание)
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)  # если же свободных столов не осталось, то помещаем гостя в очередь queue
                print(f'{guest.name} в очереди')

    def table_free(self):
        '''поиск свободного стола'''
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def discuss_guests(self):
        '''Этот метод имитирует процесс обслуживания гостей.'''
        while not self.queue.empty() or self.guest_serviced():  # если очередь не пустая или хотя бы один стол занят.
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Если за столом есть гость и гость(поток) закончил
                                                                # приём пищи(поток завершил работу - метод is_alive)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None                          # стол освободился

                if not self.queue.empty() and table.guest is None:  # Если очередь ещё не пуста (метод empty) и один из
                    # столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get())
                    guest_next = self.queue.get()  # получаем из очереди имя(объект queue) следующего гостя
                    table.guest = guest_next  # сажаем за освободившийся стол следующего гостя
                    print(f'{guest_next.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    guest_next.start()  # и запускаем потока следующего Гостя (обслуживание)

    def guest_serviced(self):  # Проверка наличия гостей в кафе
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


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
