m = 4
i = 1

for i in range(1,m+1):
    for k in range (i,m*m+1,m):
        print(k, end=" ")
    print()