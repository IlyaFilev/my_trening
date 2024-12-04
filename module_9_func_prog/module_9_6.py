'''Генераторы'''


def all_variants(text):
    for j in range(len(text)):
        for i in range(len(text) - j):  # j возрастает => i убывает, возрастает кол. символов в выдаче: 1, 2, 3,..
            yield text[i:i + j + 1]  # Задаём начало и срез для строки (+1 для сдвига диапазона)



a = all_variants("abcd")
for i in a:
    print(i)
'''
a
b
c
d
ab
bc
cd
abc
bcd
abcd
'''