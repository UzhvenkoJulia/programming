n = int(input())
cubes = []
i = 1
while i ** 3 < n:
    cubes.append(i ** 3)
    i += 1
for cube in cubes:
    print(cube, end=" ")