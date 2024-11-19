# "Try и Except"

def add_everything_up(a, b):
    try:
        result = a + b
        if type(result) == float:
            return round(result, 3)
        else:
            return result
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7.0))
print(add_everything_up('яблоко', 'Груша'))