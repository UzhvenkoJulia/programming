m = input()
steps = 0

while m != m[::-1]:
    m = str(int(m) + int(m[::-1]))
    steps += 1

print(steps)