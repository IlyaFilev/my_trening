# "Try и Except"

def add_everything_up(a, b):
    try:
        return round((a + b), 3) # округление до 3 знака
    except TypeError:  # одно из значений строка, то конвертируем оба значения в строки и складываем
        return str(a) + str(b)


print(add_everything_up(5, 6))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7.0))
print(add_everything_up('яблоко', [1, 'd', 5]))