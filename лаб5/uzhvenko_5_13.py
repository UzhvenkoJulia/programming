n = int(input())
sequence = list(map(float, input().split()))
sum_of_positive_numbers = 0
count_of_positive_numbers = 0

for num in sequence:
    if num > 0:
        sum_of_positive_numbers += num
        count_of_positive_numbers += 1

if count_of_positive_numbers > 0:
    average_positive = sum_of_positive_numbers / count_of_positive_numbers
    print('{:.2f}'.format(average_positive))
else:
    print('Not Found')