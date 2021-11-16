n = 2
x = 1
sum = 1
num = 1
if x == 0:
    print('Zero denominator')
else:
    for i in range(1, n + 1):
        num *= i
        den = x ** i
        sum += num/den

    print(sum)