# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки
# обʼєкти класу Point.
# Використовуйте property
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет атрибут, що містить площу трикутника (за допомогою property).
# Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
#
import math

class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value
    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, int) or not isinstance(y_coord, int):
            raise TypeError
        self.x = x_coord
        self.y = y_coord


point1 = Point(2, 3)
point2 = Point(4, 1)



class Line:
    begin = None
    end = None

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    @property
    def get_length(self):

        return 0
line1 = Line(point1, point2)


print(line1.get_length)

class Triangle:
    len_1 = None
    len_2 = None
    len_3 = None

    def __init__(self, begin_point, end_point):
        self.len_1 = self.begin.x - self.end.x
        self.len_2 = self.begin.y - self.end.y
        self.len_3 = ((self.len_1) ** 2 + (self.len_2) ** 2) ** 0.5

    @property
    def get_triangle(self):
        s = abs(((self.len_1) + (self.len_2) + (self.len_3)) / 2)
        return math.sqr(s * (s - (self.len_1)) * (s - (self.len_2)) * (s - (self.len_3)))

    len1 = Line(point1, point2)







