class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'

    # def __len__(self):
    #     return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            print('Верно')
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # __str__
print(h2)

# print(h1 == h2)  # __eq__
# print(h1)

h1 = h1 + 10  # __add__
print(h1) # НЕ выводит Полное название объекта и кол-во Этажей
print(h1 == h2)

# h1 += 10  # __iadd__
# print(h1)

# h2 = 10 + h2  # __radd__
# print(h2)

# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
