# "Сложные моменты и исключения в стеке вызовов функции"
def personal_sum(numbers):
    result = 0
    for i in numbers:
        result += i
    incorrect_data = 1
    return result, incorrect_data

def calculate_average(numbers): # Среднее арифметическое - сумма всех данных делённая на их количество.
    return personal_sum(numbers)[0]/len(numbers)





print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать