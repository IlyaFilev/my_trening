# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    elif int(str_number[-1]) == 0: # если в number последняя цифра 0, то не учитываем.
        return first*get_multiplied_digits(int(str_number[1:-1]))
    else: # При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
        return first*get_multiplied_digits(int(str_number[1:]))


result = (get_multiplied_digits(10550))
print(result)
