'''Введение в потоки
Задача "Потоковая запись в файлы"'''
import time
import threading

def write_words(word_count, file_name): #  word_count - количество записываемых слов
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'\nКакое-то слово № {i}')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')

start = time.time()
write_words(10,'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
fin = time.time()
print('Работа Функции', round(fin - start, 4)) # в миллисекундах Работа Функции: 34.1195

start2 = time.time()
thread5 = threading.Thread(target=write_words, args=(10,'example5.txt'))
thread6 = threading.Thread(target=write_words, args=(30,'example6.txt'))
thread7 = threading.Thread(target=write_words, args=(200,'example7.txt'))
thread8 = threading.Thread(target=write_words, args=(100,'example8.txt'))
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
fin2 = time.time()
print('Работа потоков', round(fin2 - start2, 4)) # Работа потоков 20.0641