'''Потоки на классах'''

import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100 # кол-во врагов - по усл.задачи у всех потоков = 100

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies:
            time.sleep(1) # задержка в 1 секунду = 1 день
            days += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {days} дней, осталось {self.enemies} войнов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()