initial_list = [2,1, 1, 2, 3, 3, 2,2,2,2,1]
new_lst = []
max_list = []
for item in range(1, len(initial_list)):
    if initial_list[item] == initial_list[item-1]:
        new_lst.append(initial_list[item])
        if len(new_lst) > len(max_list):
            max_list = new_lst
            max_list.append(initial_list[item])
    else:
        new_lst = []

print(max_list)
