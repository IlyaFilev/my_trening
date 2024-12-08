'''Потоки на классах'''

import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100  # кол-во врагов - по усл.задачи = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemies:
            time.sleep(1) # задержка в 1 секунду = 1 день
            days += 1
            enemies -= int(self.power)
            print(f'{self.name} сражается {days} дней, осталось {enemies} войнов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()