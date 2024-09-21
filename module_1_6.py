my_dict = {'Иван': 1998, 'Мария': 2000, 'Сергей': 2001}
print(my_dict)
print(my_dict.get('Иван'))
print(my_dict.get('Владимир', 'Такого ключа нет'))
my_dict.update({'Саша': 2003, 'Галя': 2004})
print(my_dict.pop('Мария'))
print(my_dict)
my_set = {1, 1, 3, 3, 4, 'son', True, 'son', True, 0.2, 0.2, 0.3}
print(my_set)
my_set.add(8)
my_set.add(10)
my_set.remove('son')
print(my_set)