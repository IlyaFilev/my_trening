# "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):  # Среднее арифметическое всех чисел
    try:
        res_inc_data = personal_sum(numbers)
        return res_inc_data[0]/(len(numbers)-res_inc_data[1])
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(888)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
try:
    print(f'Результат 5: {calculate_average(стока)}')
except NameError:
    print('Следи за тем, что вводишь, Бро!')