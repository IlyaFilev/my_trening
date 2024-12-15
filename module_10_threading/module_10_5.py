'''Многопроцессное программирование
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
'''
import multiprocessing
import time
from multiprocessing.managers import PoolProxy


def read_info(name):
    all_data = []
    file = open(name, mode='r', encoding='utf8')
    line = True
    while line:
        line = file.readline()
        all_data.append(line)
    file.close()

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'] #

'''Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
 предварительно закомментировав другой.'''
# start = time.time()
#
# for name_file in files:
#     read_info(name_file)
#
# fin = time.time() - start
# print(f'время выполнения линейного подхода: {round(fin, 4)}c.')

# время выполнения линейного подхода: 3.7957c.

if __name__ == '__main__':
    start2 = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files) # позволяет параллельно выполнять функции на нескольких процессах

    fin2 = time.time() - start2
    print(f'время выполнения мультипроцессом: {round(fin2, 4)}c.')

# время выполнения мультипроцессом: 1.4914c.