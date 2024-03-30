import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        base_average = (self.a + self.b) / 2
        return base_average * self.c


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2


def read_input(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            figure_type = parts[0] # перший елемент рядка
            params = list(map(float, parts[1:]))
            if figure_type == 'Triangle' and len(params) == 3:
                a, b, c = params

                if a + b > c and a + c > b and b + c > a:
                    figures.append(Triangle(a, b, c))
                else:
                    print("дані для трикутника якісь некоректні:", params)
            elif figure_type == 'Rectangle' and len(params) == 2:
                figures.append(Rectangle(*params))

                '''Цей рядок коду ДОДАЄ НОВИЙ ЕКЗЕМПЛЯР КЛАСУ Rectangle ДО СПИСКУ figures!!! 
                Параметри, які передаються до конструктора класу Rectangle, передаються як аргументи під час виклику методу (append).
                У цьому випадку (*params) використовується для передачі аргументів конструктору класу Rectangle. 
                Він розгортає список params, передаючи кожен елемент окремо ЯК АРГУМЕНТ. 
                Такий синтаксис використовується, коли кількість параметрів, які потрібно передати, 
                відома під час виконання програми, і це спрощує передачу аргументів функціям або методам.
                Отже, якщо params містить два числа, вони будуть передані як два аргументи конструктору класу Rectangle, 
                які представляють довжину та ширину прямокутника. 
                Такий екземпляр потім додається до списку (figures).'''

            elif figure_type == 'Trapezium' and len(params) == 4:
                figures.append(Trapezium(*params))

            elif figure_type == 'Parallelogram' and len(params) == 3:
                figures.append(Parallelogram(*params))
            elif figure_type == 'Circle' and len(params) == 1:
                figures.append(Circle(*params))
            else:
                print("дані для фігури некоректні:", figure_type, params)
    return figures


def find_max_area_and_perimeter(figures):
    max_area = float('-inf') # ініціалізація як від'ємна нескінченність
    max_perimeter = float('-inf')
    max_area_figure = None
    max_perimeter_figure = None
    '''(None) Це дозволяє почати з пошуку найбільшої площі та периметру з нульових значень, 
    і під час обходу фігур ці значення будуть оновлюватися, 
    якщо знайдуться фігури з більшими площею або периметром.'''

    for figure in figures:
        if hasattr(figure, 'area'):

            '''hasattr() - це функція мови програмування Python, яка приймає два аргументи: 
            об'єкт і назву атрибуту (або методу) та повертає True, якщо об'єкт має такий атрибут або метод, і False, якщо не має. 
            Ця функція корисна для динамічного перевірки наявності атрибутів або методів в об'єктах перед їх використанням'''

            area = figure.area()
            if area > max_area:
                max_area = area
                max_area_figure = figure

        if hasattr(figure, 'perimeter'):
            if isinstance(figure, Circle): # перевірка типу фігури (чи є вона колом)
                perimeter = figure.circumference()
            else:
                perimeter = figure.perimeter()

            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_perimeter_figure = figure

    return max_area_figure, max_perimeter_figure


input_files = ['input01.txt', 'input02.txt', 'input03.txt']

for filename in input_files:
    print(f"файл в роботі {filename}:")

    figures = read_input(filename)

    for figure in figures:
        if isinstance(figure, Circle): # екземпляр певного класу, перевірка
            print(f"довжина кола: {figure.circumference()}")
        else:
            print(f"периметр {figure.__class__.__name__}: {figure.perimeter()}")

    max_area_figure, max_perimeter_figure = find_max_area_and_perimeter(figures)
    print("фігура з найбільш площею:", max_area_figure.__class__.__name__)
    print("фігура з найбільш периметром:", max_perimeter_figure.__class__.__name__)
    print()