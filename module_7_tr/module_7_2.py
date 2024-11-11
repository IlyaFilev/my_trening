# "Позиционирование в файле".
# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.

def custom_write(file_name, strings):  # название файла для записи И список строк для записи.
    strings_positions = {}
    str_n = 0
    file = open(file_name, 'w', encoding='utf-8')  #
    for i in strings:
        str_n += 1  # счетчик строк
        beginning_wrt = file.tell()  # номер байта начала строки перед записью
        file.write(f'{i}\n')  # Добавление строки в файл с переносом
        strings_positions.update({(str_n, beginning_wrt): i})  # добавление в словарь
    file.close()  # закрытие файла
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
