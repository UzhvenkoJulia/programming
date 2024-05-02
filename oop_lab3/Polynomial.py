import rational_numbers


class Polynomial(dict):

    '''Реалізуйте клас для роботи з многочленами з довільними коефіцієнтами.
        Клас Polynomial має наслідуватись від словника і, відповідно,
        представляти многочлен як словник <степінь: коефіцієнт>.
        Імплементуйте наступні методи..
        і напишіть | мінімальні демонстраційні тести | до них'''

    def __init__(self, arg, coeff_type=float):
        super().__init__()
        self.coeff_type = coeff_type
        if isinstance(arg, str):
            self._parse_string(arg) # виклик приватного методу, якщо так
        elif isinstance(arg, dict):
            for deg, coeff in arg.items():
                self[deg] = coeff  # степенева змінна deg
        elif isinstance(arg, list):
            for i, coeff in enumerate(arg):
                self[i] = coeff
        elif isinstance(arg, (int, float)):  # число ціле, десяткове?
            self[0] = coeff_type(arg)
        else:
            raise ValueError("формат многочлена задано неправильно")
        self._reduce()

    '''Тепер реалізую метод _parse_string, який буде парсити рядок з многочленом'''

    def _parse_string(self, string):
        tokens = string.split('+')
        for token in tokens:
            token = token.strip()
            if token:
                parts = token.split('x^') # токен на дві частини, роздільник - x
                if len(parts) == 1:
                    if 'x' in parts[0]:
                        coeff = parts[0].split('x')[0].strip()
                        deg = 1  # встановлюємо степінь на 1
                    else:
                        coeff = parts[0].strip() # отримуємо коеф - (частину до x)
                        deg = 0
                else:
                    coeff = parts[0].strip()
                    deg = int(parts[1].replace('^', '').strip()) # ми використовуємо другий елемент, тобто як степінь
                self[deg] = self.coeff_type(coeff)

    def copy(self):
        return Polynomial(self, self.coeff_type)

    def as_type(self, coeff_type):
        new_poly = Polynomial(coeff_type=self.coeff_type)
        for deg, coeff in self.items():
            new_poly[deg] = coeff_type(coeff)
        return new_poly

    def __str__(self):
        terms = []
        for deg in sorted(self.keys(), reverse=True):  # сортування відбувається у зворотньому порядку
            coeff = self[deg]
            if coeff < 0:
                term_str = f"- {-coeff} * x^{deg}"  # додаємо знак мінус перед коефіцієнтом
            else:
                term_str = f"{coeff} * x^{deg}"
            terms.append(term_str)
        polynomial_str = " + ".join(terms)
        return polynomial_str

    def __repr__(self):
        terms = []
        for deg in sorted(self.keys(), reverse=True):  # відсортований порядок за зменшенням степеня
            coeff = self[deg]
            term_str = f"{coeff}: {deg}"
            terms.append(term_str)
        polynomial_repr = "{" + ", ".join(terms) + "}"
        return polynomial_repr

    def __iter__(self):
        keys = sorted(self.keys())
        for deg in keys[::-1]:
            yield deg, self[deg]

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            # іф 'other' - число, конвертую його у многочлен нульового степеня
            if isinstance(other, (int, float)):
                other = Polynomial({0: other}, coeff_type=self.coeff_type)
            else:
                raise TypeError("тип операндів непідтримуваний для + : '{}' та '{}'".format(type(self), type(other)))

        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)  # конвертація
        result = self.copy()

        '''Якщо коефіцієнт для даної степені вже існує у результаті, то він додається до нього. 
        Якщо коефіцієнт для даної степені відсутній, то він додається зі значенням за замовчуванням 0.'''

        for deg, coeff in other.items():
            result[deg] = result.get(deg, 0) + coeff
        return result

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        elif not isinstance(other, Polynomial):
            raise TypeError("непідтримуваний тип операнду")

        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)

        result = Polynomial(self.copy())
        for power, coeff in other.items():
            result[power] = result.get(power, 0) - coeff
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial({0: other})
        elif not isinstance(other, Polynomial):
            raise TypeError("непідтримуваний тип операнду")

        if self.coeff_type != other.coeff_type:
            other = other.as_type(self.coeff_type)

        result = {}
        for power1, coeff1 in self.items():
            for power2, coeff2 in other.items():
                product = coeff1 * coeff2
                if product != 0:
                    result[power1 + power2] = result.get(power1 + power2, 0) + product
        return Polynomial(result, coeff_type=self.coeff_type)

    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("значення аргументу повинно бути числом!!")

        result = 0
        for power, coeff in self.items():
            result += coeff * (value ** power)
        return result

    def __truediv__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("непідтримуваний тип операнду, переконайтеся, що використовуєте правильні типи даних для ваших операцій")

        result = {}
        for power, coeff in self.items():
            result[power] = coeff / value
        return Polynomial(result, coeff_type=self.coeff_type)

    def derivative(self):
        if not self or len(self) == 1:  # перевірка на порожній многочлен або на одиничний член!!
            return Polynomial({}, coeff_type=self.coeff_type)

        result = {}
        for power, coeff in self.items():
            if power != 0:  # похідна константи = 0 !!
                result[power - 1] = coeff * power
        return Polynomial(result, coeff_type=self.coeff_type)

    '''primitive(self): повернути первісну многочлена (ігнорувати +С)'''

    def primitive(self):
        result = {}
        for power, coeff in self.items():
            if power != 0:
                result[power + 1] = coeff / (power + 1)
            else:
                result[1] = coeff
            if power + 1 not in self.keys():
                result[power + 1] = 0
        return Polynomial(result, coeff_type=self.coeff_type)

        # ділення многочленів з остачею

    '''def __divmod__(self, other):
            if not isinstance(other, Polynomial) or other.is_zero():
                raise ValueError("другий операнд має бути ненульовим многочленом")

            fraction = Polynomial({0: 0})
            remainder = self.copy()

            # Спочатку частка і залишок ініціалізуються таким чином: частка - нульовий многочлен,
            # а залишок - копія першого многочлена, який ми ділимо на другий.
            # Далі ми будемо змінювати ці значення в процесі ділення.

            while remainder.degree() >= other.degree(): # використовується, коли степінь діленого многочлена більший або рівний степені дільника
                # отримання степеня і коефіцієнта першого члена поточного многочлена
                lead_degree = remainder.leading_degree()
                lead_coeff = remainder[lead_degree]

                other_lead_degree = other.leading_degree()
                other_lead_coeff = other[other_lead_degree]

                div_coeff = lead_coeff / other_lead_coeff

                fraction_term = Polynomial({lead_degree - other_lead_degree: div_coeff})

                fraction += fraction_term
                remainder -= other * fraction_term
                return fraction, remainder'''

    def _reduce(self):
        '''Маю многочлен, треба видалити степені з нульовими коефіцієнтами'''
        delete = []
        for deg, coeff in self.items():
            if coeff == 0:
                delete.append(deg)
        for deg in delete:
            del self[deg]

    '''def gcd(self, other):
        """Знаходження найбільшого спільного дільника двох многочленів.
        Args:
            other (Polynomial): інший многочлен
        Returns:
            Polynomial: нсд
        """
        dividend = self.copy()
        divisor = other.copy()

        while divisor:
            dividend, divisor = divisor, dividend % divisor

        return dividend'''

    def newton_method(self, initial_guess, tolerance=1e-6, max_iterations=100):  # ітераційний процес
        """Знаходження наближеного кореня многочлена, методом Ньютона
        Args:
            initial_guess (float): початкове наближення для кореня
            tolerance (float, optional): допустима похибка
            max_iterations (int, optional): max к-сть ітерацій.
            --------------------(не забути!!)--------------------
                            За замовчуванням 100
        Returns:
            float: значення кореня многочлена або None, якщо корінь не був знайдений
        """
        x = initial_guess
        iteration = 0

        while iteration < max_iterations:
            f_x = self(x)
            if abs(f_x) < tolerance:
                return x

            f_prime_x = self.derivative()(x)
            if f_prime_x == 0:
                # для уникнення ділення на нуль!!
                return None

            x -= f_x / f_prime_x  # ---------> наближення до кореня
            iteration += 1

        return None

    def lagrange_interpolation(points):

        """
        Створення інтерполяційного многочлена Лагранжа за n+1 точками
        (використовуючи множення многочленів)
        Інтерполювати многочлен будемо за списком кортежів (x, y)
        """

        result = Polynomial({0: 0})  # ініціалізую результат нульовим многочленом
        for i, (x_i, y_i) in enumerate(points):
            term = Polynomial({1: 1})  # ініціалізую множник 1
            for j, (x_j, _) in enumerate(points): # _ - використовується для ігнорування другого елемента кортежу
                if i != j:
                    # + множник (x - x_j) / (x_i - x_j)
                    factor = Polynomial({1: -x_j, 0: 1}) / (x_i - x_j)
                    term *= factor
            result += term * y_i
        return result

    @classmethod
    def gcd(cls, poly1, poly2):
        """
        Знаходження НСД двох многочленів за допомогою алгоритму Евкліда
        """
        if not all(isinstance(poly, Polynomial) for poly in (poly1, poly2)):
            raise TypeError("аргументи повинні бути екземплярами класу Polynomial!!")

        while poly2:
            quotient, remainder = Polynomial.divide_with_remainder(poly1, poly2)
            poly1 = poly2
            poly2 = remainder

        return poly1

    # не реалізувала я метод класу Polynomial, який виконує ділення многочлена dividend
    # на многочлен divisor, повертаючи частку та залишок у вигляді кортежу

# швидкі тестикі

p1 = Polynomial("7x^2 + 4x + 1")
p2 = Polynomial("4x^2 + 5x + 3")
p3 = p1 + p2
print("p1 + p2:", p3)
p4 = p1 - p2
print("p1 - p2:", p4)
p5 = p1 * p2
print("p1 * p2:", p5)
print("p1(2):", p1(2))
p6 = p1 / 2
print("p1 / 2:", p6)

print("Похідна від p1:", p1.derivative())
print("Первісна від p1:", p1.primitive())

p = Polynomial({3: 2, 2: -4, 1: 7, 0: -2})
initial_guess = 3.0
root = p.newton_method(initial_guess)
if root is not None:
    print("корінь наближений:", root)
else:
    print("відповідь не знайдено чи метод Ньютона не збігся")

points = [(0, 2), (4, 6), (2, 4)]
lagrange_poly = Polynomial.lagrange_interpolation(points)
print("інтерполяційний многочлен Лагранжа:", lagrange_poly)
