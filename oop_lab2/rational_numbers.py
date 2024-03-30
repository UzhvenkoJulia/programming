from math import gcd

class Rational_numbers:

    __slots__ = ["_n", "_d"]
    # кожний об'єкт класу може мати тільки атрибути _n та _d, які відповідають чисельнику і знаменнику раціонального числа
    # numerator (_n) - чисельник раціонального числа; denominator (_d) - знаменник раціонального числа

    def __init__(self, n, d) -> None:

        '''Раціональне число -- це нескоротний (!!) дріб m / n, де m,n -- цілі числа, до того ж (n > 0).
    Скорочення і приведення до нормальної форми має відбуватись ще на етапі конструктора і більше ніде.
    Раціональне число має бути immutable.
    Скористаюся викликом приватного (статичного) методу _reduce().'''

        if d == 0:
            raise ValueError("denominator - 0, неможливо ")
        self._n, self._d = self._reduce(n, d)


    @staticmethod
    def _reduce(n, d): # _reduce виконує скорочення раціонального числа, знаходячи їхній нсд та ділячи чисельник і знаменник на цей нсд
        while gcd(n, d) != 1: # потребується перевірка (не взаємно прості, взаємно прості), а потім я повинна отримати цілі числа в результаті
            gcd_value = gcd(n, d)
            n //= gcd_value
            d //= gcd_value
        return n, d


    @property
    def numerator(self):
        return self._n


    @property
    def denominator(self):
        return self._d


    @classmethod
    def from_string(cls, string):

        '''конструктор from_string -- класовий метод, який створює раціональне число з рядку.
        Рядок повинен мати вигляд m / n (можливо з пробілами або мінусами) АБО це звичайне ціле число.
        використання методу strip(), щоб видалити пробіли з початку та кінця рядка, а потім викликати split("/"),
        щоб розділити рядок на чисельник та знаменник за допомогою символу "/".
        якщо список має довжину 2 - отримано як чисельник, так і знаменник вже.
        (якщо довжина 1), припущення!!, що отриманий рядок представляє ціле число, а значення знаменника встановлюється як 1
        далі йде перетворення у цілі числа'''

        k = string.strip().split("/")
        if len(k) == 2:
            numerator = k[0]
            denominator = k[1]
        else:
            numerator = k[0]
            denominator = "1"
        numerator = int(numerator)
        denominator = int(denominator)
        return cls(numerator, denominator)


    def __add__(self, something):
        '''додавання (магічний метод __add__):
        передбачити в обидва боки
        передбачити додавання звичайного числа
        викликає конструктор класу при поверненні результату'''
        if isinstance(something, int):
            something = Rational_numbers(something)
            # сума двох раціональних чисел; (numerator1 * denominator2 + numerator2 * denominator1) / (denominator1 * denominator2)
        return Rational_numbers(self.numerator * something.denominator + something.numerator * self.denominator, self.denominator * something.denominator)


    def __radd__(self, something):
        return something.__add__(self)


    def __sub__(self, something):
        if isinstance(something, int):
            something = Rational_numbers(something)
        return Rational_numbers(self.numerator * something.denominator - something.numerator * self.denominator, self.denominator * something.denominator)


    def __rsub__(self, something):
        return something.__sub__(self)


    def __mul__(self, something):
        if isinstance(something, int):
            something = Rational_numbers(something)
        return Rational_numbers(self.numerator * something.numerator, self.denominator * something.denominator)


    def __rmul__(self, something): # __rmul__ визначає, як множення виглядає у випадку, коли об'єкт класу знаходиться справа від оператора *
        return something.__mul__(self)


    def __truediv__(self, something):
        if isinstance(something, int):
            something = Rational_numbers(something)
        if something.numerator == 0:
            raise ValueError("/ (:) на 0")
        return Rational_numbers(self.numerator * something.denominator, self.denominator * something.numerator)


    def __rtruediv__(self, something):
        if self.numerator == 0:
            raise ValueError("/ (:) на 0")
        return something.__truediv__(self)


    def __abs__(self):
        '''Цей метод створює новий об'єкт класу Rational_numbers,
        де чисельник і знаменник рівні відповідним абсолютним значенням чисельника і знаменника поточного об'єкту.
        Таким чином, він повертає абсолютне значення раціонального числа.'''
        return Rational_numbers(abs(self.numerator), abs(self.denominator))


    def sign(self): # знаки дробів
        if self.numerator > 0 and self.denominator > 0:
            return 1
        if self.numerator < 0 or self.denominator < 0:
            return -1


    def integer(self):
        if self.denominator == 1: # а це раціональне число є цілим?
            return True
        else:
            return False


    def __eq__(self, something):
        if isinstance(something, int):
            something = Rational_numbers(something)
        return self.numerator == something.numerator and self.denominator == something.denominator


    def inverse(self):
        if self.numerator == 0:
            raise ValueError("denominator оберненого дробу - 0")
        return Rational_numbers(self.denominator, self.numerator)


    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator / self.denominator)


    def __repr__(self):
        return f"Rational_numbers(numerator = {self.numerator}, denominator = {self.denominator})"