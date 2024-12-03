'''Итераторы'''

class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.pointer = start
        self.stop = stop
        if step == 0:
            raise StepValueError(f'шаг не может быть равен 0')
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step < 0 and self.pointer < self.stop or self.step > 0 and self.pointer > self.stop:
                raise StopIteration
        else:
            self.pointer += self.step
            return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print('II')
for i in iter3:
    print(i, end=' ')
print('III')
for i in iter4:
    print(i, end=' ')
print('IV')
for i in iter5:
    print(i, end=' ')
print('V')
