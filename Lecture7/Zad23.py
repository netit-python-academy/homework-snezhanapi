

n = input()
k = input()
sum = 1
sum2 = 1
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
        else:
            sum2 *= i
    print(sum2/sum)
else:
    print("K must be < N")