n = int(input())
o = input()

cube_list = str(o)
my = {}
for letter in cube_list:
    if letter not in my:
        my[letter] = cube_list.count(letter)

o = 0

for key, value in my.items():
    if value % 2 != 0:
        o += 1
        print(key)
if o == 0:

    print("Ok")