from rational_numbers import Rational_numbers

with open("input1.txt", "r") as file:
    numbers = []
    for line in file:
        line = line.strip()
        numbers.append(Rational_numbers.from_string(line))

max_num = None # початкове значення встановлюється на None, а потім воно буде оновлюватися під час обходу чисел у файлі
max_abs_num = None # за модулем
summ_num = 0

for num in numbers: # для того, щоб порівняти дроби наші, я звожу їх до спільного дільника і порівнюю їх чисельники
    if max_num is None or (num.denominator > 0 and num.numerator > 0 and num.numerator * max_num.denominator > max_num.numerator * num.denominator):
        max_num = num
    abs_num = Rational_numbers.__abs__(num)
    if max_abs_num is None:
        max_abs_num = num
    else:
        max_abs_num = Rational_numbers.__abs__(max_abs_num)
        if abs_num.numerator * max_abs_num.denominator > max_abs_num.numerator * abs_num.denominator:
            max_abs_num = num
    summ_num = Rational_numbers.__add__(summ_num, num)

arithmeticmean = str(summ_num / Rational_numbers(len(numbers), 1))

print("max_num:", max_num)
print("max_abs_num:", max_abs_num)
print("середнє арифметичне значення:", arithmeticmean)