# першим ділом я створюю модуль


#  треба мати функцію, щоб вводити матрицю, розмірність типу може мати, яку забажаю ??
def input_crazymatrix(n):  # квадратна матриця!!
    array = []
    for i in range(n):
        line = list(map(float, input(f"значення {i + 1}: ").split()))  # потрібні списки чисел - перетворення значень в список чисел; число, плаваюча точка; поділ типу це пробіли, cool, додаємо до i 1, щоб з нуля нічого тут не починалося
        array.append(line)
    return array  # повернення, отримання готового вже продукту

def print_crazymatrix(array):  # нам треба матрицю нашу десь бачити
    for line in array:
        print(" ".join(map(str, line)))  # тут, сподіваюся, лежить магічне виведення елементів списку, розділених пробілами ??

def crazymatrix_multiply(m1, m2):  # тут все зрозуміло, множимо
    boom = []
    for a in range(len(m1)): # + довжина
        line = []
        for b in range(len(m2[0])):  # прикольна штука [0] - початок з 0, перший рядок; двовимір списк (матриця)
            output = sum(m1[a][f] * m2[f][b] for f in range(len(m2)))  # якщо я не плутаю, то f - стовпець рядка i; типу + індекс елемента в рядку нашому i;
            # тут повина обчисл кожен елемент множ матриці на матрицю як суму добутків
            line.append(output)
        boom.append(line)
    return boom

def crazymatrix_vector_multiply(m, v):  # ігри з вектором; м на в
    boom = []
    for a in range(len(m)):
        output = sum(m[a][b] * v[b] for b in range(len(v)))  # обчисл кожен елемент резулт наш вектора як суму добутків; v[b] - значення вектора v з позицією b
        boom.append(output)
    return boom

def vector_crazymatrix_multiply(v, matrix):  # в на м
    boom = []
    for a in range(len(matrix[0])):
        value = sum(v[b] * matrix[b][a] for b in range(len(v)))
        boom.append(value)
    return boom

def intrchg_line(m, line01, line02):
    m[line01], m[line02] = m[line02], m[line01]

def intrchg_columns(m, c01, c02):  # міняю стовпці
    for row in m:
        row[c01], row[c02] = row[c02], row[c01]

def surprise_line(m, line_numb):  # рядок матриці -> по номеру самого цього рядка
    return m[line_numb]

def v_multiply_tyda_scl(v, scl):  # вектора * скаляр
    return [suda * scl for suda in v]

def subtract_v_from_line(m, v):  # всі рядки м - (мінус) вектор
    for a in range(len(m)):
        m[a] = [m[a][b] - v[b] for b in range(len(v))]
