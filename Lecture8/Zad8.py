initial_list = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
sum = 0
max_sum = sum(initial_list[0:3])
for item in range(2,len(initial_list)-3):
    sum = sum(initial_list[item:item+3])
    if max_sum < sum:
        max_sum == sum
print(sum)
print(max_sum)