# Дополнительное практическое задание по модулю
import math


class Figure:
    sides_count = 0
    filled = True

    def __init__(self, color, *args_sides):
        if self.__is_valid_color(color) == color:
            self.__color = color                # список цветов в формате RGB
        if self.__is_valid_sides(*args_sides) is True:
            self.__sides = args_sides           # (список сторон (целые числа))
        else:
            list_one = []
            for i in range(self.sides_count):
                list_one.append(1)
            self.__sides = list_one
            print('Некоректный ввод количества сторон, будет создан единичный список сторон фигуры')

    def get_color(self):                    # возвращает список RGB цветов
        return list(self.__color)

    def __is_valid_color(self, new_color): # проверяет корректность переданных значений перед установкой нового цвета
        flag = 0
        for i in new_color:
            if 255 >= i >= 0 == i % 1:
                flag += 1
        if flag == 3:
            self.__color = new_color
            return self.__color
        else:
            print('Не корректные параметры цвета: r, g и b - целые числа в диапазоне от 0 до 255 (включительно), внесение/изменение не произойдет')

    def set_color(self, *args_new_color):           # принимает новый цвет
        self.__is_valid_color(args_new_color)

    def __is_valid_sides(self, *args_sides):        # проверка сторон
        flag = 0
        for i in args_sides:
            if i > 0 and i % 1 == 0:
                flag += 1
        if flag == len(args_sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):                # возвращает список сторон фигуры (длин), не работает в Кубе, тк __sides переопределен
        return list(self.__sides)

    def __len__(self):                  # возвращает периметр фигуры (непонтно зачем __len__ по условию???)
        return sum(self.get_sides())

    def set_sides(self, *new_sides):    # принимает новые значения сторон, если их количество не подходит - не меняет
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            print('Введено не корректное значение сторон, внесение/изменение не произойдет')


class Circle(Figure):
    sides_count = 1
    # __radius = Figure.__len__() / (2 * math.pi) #  !? тут не работает код, нужно определять для экземляра, а не класса

    def __init__(self, color, *args_sides):
        super().__init__(color, *args_sides)
        self.__radius = self.__len__() / (2 * math.pi)  # радиус, доп. атрибут экземпляра

    def get_square(self):       # возвращает площадь круга
        return math.pi * self.__radius ** 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args_sides):
        super().__init__(color)
        list_sides = []
        if len(args_sides) == 1:
            for i in range(self.sides_count):
                list_sides.append(args_sides[0])
            self.__sides = list_sides  # переопределил __sides сделав список из 12 один-ых сторон (передаётся 1 сторона)
        else:
            for i in range(self.sides_count):
                list_sides.append(1)
            self.__sides = list_sides    # переопределил __sides

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_sides(self):                # возвращает список сторон фигуры (длин), ДУБЛЬ в Кубе, тк __sides переопределен
        return list(self.__sides)

# F = Figure((0, 150, 255), )
# F.set_color(0, 1, 250)
# print(F._Figure__is_valid_sides(1))
# print(F.get_sides())
# print(F.__len__())
# F.set_sides(9)
# C = Circle((1, 2, 3), 6)

# Проверка
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # !!!????
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())





