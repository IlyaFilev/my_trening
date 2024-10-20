# Доп. задание по модулю 3
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(lst):
    total=0
    for item in lst:
        if isinstance(item, int):
            total += item           # подсчет цифр
        elif isinstance(item, str):
            for i in item:
                if i.isdigit(): # поиск числа в строке
                    a = int(i)  # если найдено, то меняем тип со строки на целое число
                    total += a     # подсчет цифр, найденных в строке
                else:
                    total += 1     # подсчет строк
        elif isinstance(item, list):
            total += calculate_structure_sum(item)
        elif isinstance(item, set):
            total += calculate_structure_sum(item)
        elif isinstance(item, tuple):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            dict_item = item.items() # достаем из словаря ключи и значения в виде картежа
            total += calculate_structure_sum(dict_item)
    return total


result_ = calculate_structure_sum(data_structure)
print(result_)