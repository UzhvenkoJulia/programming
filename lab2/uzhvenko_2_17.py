Cx, Cy = map(int, input().split())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

# Перевіряємо, чи точка C належить прямій AB
if (Bx - Ax) * (Cy - Ay) == (By - Ay) * (Cx - Ax):
    print("YES")
else:
    print("NO")

# Перевіряємо, чи точка C належить променю AB
if (Bx - Ax) * (Cy - Ay) == (By - Ay) * (Cx - Ax) and (Bx - Ax) * (Cx - Ax) + (By - Ay) * (Cy - Ay) >= 0:
    print("YES")
else:
    print("NO")

# Перевіряємо, чи точка C належить відрізку AB
if (Bx - Ax) * (Cy - Ay) == (By - Ay) * (Cx - Ax) and (Bx - Ax) * (Cx - Ax) + (By - Ay) * (Cy - Ay) >= 0 and (Ax - Bx) * (Cx - Bx) + (Ay - By) * (Cy - By) >= 0:
    print("YES")
else:
    print("NO")