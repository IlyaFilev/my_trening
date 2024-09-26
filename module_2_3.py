# Задача "Нули ничто, отрицание недопустимо!":
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
np = 0
while True:
    if np == len(my_list):
        print('Конец списка')
        break
    else:
        if my_list[np] > 0:
            print(my_list[np])
            np = np + 1
            continue
        elif my_list[np] == 0:
                np = np + 1
                continue
        else:
            print('Первое отрицательное')
            break



