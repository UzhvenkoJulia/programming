def read_file(file_path):  # ми відкриваємо файл, зчитуємо вміст файлу
    with open(file_path, "r") as file:
        content = file.readlines()
    return content


def parse_numb(line):  # розділяємо рядок на окремі числа, -> список цілих чисел
    return [int(num) for num in line.split()]


def count_even_numb(numb):  # обчисл к-сть парних чисел
    return sum(1 for num in numb if num % 2 == 0)


def count_squares_of_odd_numb(numb):  # обчисл к-сть квадратів непар чисел
    return sum(1 for num in numb if num % 2 != 0) ** 2


def f_difference(numb):  # найбільш пар і найменш непар числ, їх різниця
    e_numb = [num for num in numb if num % 2 == 0]
    o_numb = [num for num in numb if num % 2 != 0]

    m_e = max(e_numb)
    m_o = min(o_numb)

    return m_e - m_o


def l_increasing_sequence_length(numb):  # найдовш зростаюч послідовність, к-сть компонент у ній
    long_sequence = []
    curr_sequence = [numb[0]]

    for num in numb[1:]:
        if num > curr_sequence[-1]:
            curr_sequence.append(num)
        else:
            if len(curr_sequence) > len(long_sequence):
                long_sequence = curr_sequence.copy()
            curr_sequence = [num]

    return len(long_sequence)


file_p = 'лаб13.txt'
content = read_file(file_p)

for line in content:
    numb = parse_numb(line)
    print(f'к-сть парних чисел: {count_even_numb(numb)}')
    print(f'к-сть квадратів непарних чисел: {count_squares_of_odd_numb(numb)}')
    print(f'різниця між найбільшим парним і найменшим непарним числами: {f_difference(numb)}')
    print(f'к-сть компонент у найдовшій зростаючій послідовності: {l_increasing_sequence_length(numb)}')