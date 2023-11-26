a, b = input(), input()
print('Ok' if all([True if n in set(a) else False for n in set(b)]) else 'No')