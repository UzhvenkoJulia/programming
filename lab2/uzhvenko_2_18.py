# Отримання координат точки (x, y) та кінців діагоналі прямокутника
x, y, x1, y1, x2, y2 = map(float, input().split())

# Перевірка, чи точка (x, y) належить прямокутнику
if (x1 <= x <= x2 or x2 <= x <= x1) and (y1 <= y <= y2 or y2 <= y <= y1):
    print(1)
else:
    print(0)