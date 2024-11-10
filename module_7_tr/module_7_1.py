from pprint import pprint

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data_products = file.read()
        file.close()
        return data_products

    def add(self, *products):
        for i in products:
            if products[i] in self.get_products():
                print(f'Продукт {super.self.name} уже есть в магазине')
            else:
                print('Добавка')
                self.__file_name = 'products.txt'
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()



class Product(Shop):

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
