m = input()
try:
    int(m)
except ValueError:
    print("Not a number")
print("---"* int(m))
for row in range(1, int(m)+1):
    for j in range(row, row + int(m)):
        print("|",end="")
        print(j % 10, end=" ")
        # if 1 <= j <= 9:
        #     print(j, end=" ")
        # else:
        #     print(str(j)[-1], end=" ")
    print("|",end="")
    print()
print("---"* int(m))