n = input()
k = input()
sum = 1
sum2 = 1
sum3 = 1
try:
    int(n)
    int(k)
except ValueError:
    print("Not a number")
if 1 < int(k) < int(n):
    for i in range(1, int(n)+1):
        if int(k) >= i:
            sum *= i
            sum2 = sum
            if int(n)-int(k) >= i:
                sum3 *=i
        else:
            sum2 *= i
    print(sum2*sum/sum3)
elif int(k) < 1 or int(n) < 1:
    print('Not in range')
else:
    print("K must be < N")