import cmath  # імпорт комплекс ч, бо корені можуть бути різними

def solve_qua_equa(a, b, c):
    assert a != 0, "коеф a заборонено дорівнювати нулю"
    discrm = b**2 - 4*a*c
    assert discrm >= 0, "твоє\Ваше рівняння розв'язків не має на множ дійсн ч"
    rstock = (-b + cmath.sqrt(discrm)) / (2*a)
    rradix = (-b - cmath.sqrt(discrm)) / (2*a)
    return rstock, rradix


try:                              # приклад
    a = float(input("коеф a: "))
    b = float(input("коеф b: "))
    c = float(input("коеф c: "))

    roots = solve_qua_equa(a, b, c)
    print("розв'язки р-ня:", roots)

except ValueError as e:  # не забути про помилки!!
    print(f"помилка: {e}")

except AssertionError as e:  # винятки; -> помилки
    print(f"помилка: {e}")
