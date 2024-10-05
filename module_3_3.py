# "Распаковка позиционных параметров"
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = [35, 5.05, 'Строка']

print_params()
print_params(8,8,8)
print_params(b = 25)
print_params(c=[1, 2, 3])