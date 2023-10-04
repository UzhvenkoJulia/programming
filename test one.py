n = int(input(" "))
product = 1
num = 1
while num <= n:
    if num % 8 == 0:
        product *= num
    num += 1
if product != 1:
    print("добуток всіх чисел від 1 до", n, "включно, які діляться на 8:", product)
else:
    print("немає чисел від 1 до", n, "включно, які діляться на 8.")