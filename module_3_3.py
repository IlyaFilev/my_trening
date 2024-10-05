# "Распаковка позиционных параметров"
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = [35, 5.05, 'Строка']
values_dict = {'a':1, "b":7.77, "c":'abc'}
values_list_2 = [88, 'String']


print_params()
print_params(8,8,8)
print_params(b = 25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

# работа со списком
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(list_my)


append_to_list(55)
append_to_list([77, 88, 99])
