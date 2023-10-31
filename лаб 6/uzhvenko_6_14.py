input_string = input()

# нижній регістр
processed_string = ''.join(input_string.split()).lower()

if processed_string == processed_string[::-1]:
    print("YES")
else:
    print("NO")