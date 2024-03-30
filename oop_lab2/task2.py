def from_string(s): # функція для перетворення рядка на список коефіцієнтів многочлена
    coefficients = []
    for term in s.split(","):
        parts = term.strip().split('/')
        if len(parts) == 2:
            numerator, denominator = map(int, parts) # цілі числа (перетворення)
            coefficients.append(numerator / denominator)
        elif len(parts) == 1:
            coefficients.append(int(parts[0]))
        else:
            raise ValueError("формат рядка неправильний: {}".format(term))
    return coefficients

def evaluate_polynomial(coefficients, x): # функція для обчислення значення многочлена в заданій точці x
    value = sum(coef * x**i for i, coef in enumerate(coefficients[::-1]))
    return value

def find_roots(coefficients):
    degree = len(coefficients) - 1
    if degree <= 2:
        if degree == 1:
            # лінійна формула для знаходження кореня многочлена першого степеня
            a, b = coefficients
            root = -b / a
            return [root] if a != 0 else []
        elif degree == 2:
            # формула дискримінанту для знаходження коренів многочлена другого степеня
            a, b, c = coefficients
            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                root1 = (-b + discriminant**0.5) / (2*a)
                root2 = (-b - discriminant**0.5) / (2*a)
                return [root1, root2]
            elif discriminant == 0:
                root = -b / (2*a)
                return [root]
            else:
                return []
    else:
        # чи всі коефіцієнти є цілими числами?
        if all(isinstance(coef, int) for coef in coefficients):
            free_coefficient = coefficients[0]
            leading_coefficient = coefficients[-1]
            rational_roots = []
            # перебираю всі можливі раціональні корені p / q
            for p in range(1, abs(free_coefficient) + 1):
                for q in range(1, abs(leading_coefficient) + 1):
                    root = p / q
                    if evaluate_polynomial(coefficients, root) == 0:
                        rational_roots.append(root)
            return rational_roots
        else:
            return None

with open('input2.txt', 'r') as file:
    coefficients = from_string(file.readline())

value_at_1 = evaluate_polynomial(coefficients, 1)
print("значення многочлена в точці 1:", value_at_1)

roots = find_roots(coefficients)
if roots is not None:
    if roots:
        print("корені многочлена:", roots)
    else:
        print("многочлен не має реальних коренів")
else:
    print("не можна використовувати перебір для многочлену з дійсними коефіцієнтами!!")
