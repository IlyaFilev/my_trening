# "Сложные моменты и исключения в стеке вызовов функции"
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            return f'Некорректный тип данных для подсчёта суммы - {i}'
    return result, incorrect_data

try:
    def calculate_average(numbers): # Среднее арифметическое - сумма всех данных делённая на их количество.
        a = 0
except TypeError:
    print('В numbers записан некорректный тип данных')
    pass
# else:
    # return personal_sum(numbers)[0]/len(numbers)


print(f'Результат 4: {calculate_average(42, 15, 36, 13)}') # Всё должно работать
