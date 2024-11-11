# Режимы открытия файлов - чтение/запись
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):  # получения текущих продуктов в списке файла 'products.txt'
        file = open(self.__file_name, 'r')  # открытие файла в режиме чтения (изменение данных невозможно)
        data_products = file.read()  # передача в data_products всего текста файла в виде строки
        file.close()  # закрытие файла
        return data_products  # возврат строки с данными файла 'products.txt'

    def add(self, *products):
        file = open(self.__file_name, 'a')  # при первом запуске в режиме appand будет создан файл 'products.txt'
        for i in products:
            t = str(i)  # объект класса Product в строковом представлении - для поиска в строке из метода get_products
            if t in self.get_products():  # получение списка продуктов из файла и поиск Продукта в нем.
                print(f'Продукт {t} уже есть в магазине')
            else:
                file.write(f'{t}\n')  # Добавление продуктов в список файла
        file.close()  # закрытие файла


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
