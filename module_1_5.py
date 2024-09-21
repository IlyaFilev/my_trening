immutabl_var = 7, True, 'apple', [5, 7, 8]
print(immutabl_var)
#immutabl_var[0] = 9 # катеж не поддерживает изменение его составляющих, исключение - список, как элемент ккортежа.
immutabl_var[3][0] = 6
print(immutabl_var)
mutale_list = [1, 'a', 'b', True]
print(mutale_list)
mutale_list[1] = 8
mutale_list[3] = False
print(mutale_list)