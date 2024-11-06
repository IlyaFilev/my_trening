# "Множественное наследование"
class Horse:

    def __init__(self, x_distance=0, sound='Frrr'):
        self.sound = sound
        self.x_distance = x_distance
        super().__init__()  # обращаемся к след. по очереди mro классу - Eagle, для получения атрибутов от "родителя"

    # причем, если написать super сразу после init на 5строке, то sound для объектов Pegasus будет наследоваться из Horse.

    def run(self, dx):
        self.x_distance += dx


class Eagle:

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)  # передаем параметры dx, dy в функции родительских классов
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance  # всё, что происходит с этими атрибутами в родительских классах,

    # мгновенно наследуется дочерним, поэтому здесь возвращаю значения этих атрибутов как объекта класса Pegasus.

    def voice(self):
        print(self.sound)  # печать значения унаследованного атрибута sound


p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice() # I train, eat, sleep, and repeat
