number = abs(int(input()))
if int(number / 100) > number % 10:
    print(int(number / 100))
elif int(number / 100) < number % 10:
    print(number % 10)
elif int(number / 100) == number % 10:
    print("=")