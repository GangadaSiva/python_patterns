n = int(input())
lists = []
for i in range(n):
    numbers = sorted(list(map(int, input().split())))
    lists.append(numbers)

output = []
for i in range(n-1):
    current_list = lists[i]
    next_list = lists[i+1]
    if current_list[1] >= next_list[0]:
        lists[i+1][0] = current_list[0]
        if current_list[1] >= next_list[1]:
            lists[i+1][1] = current_list[1]
    else:
        output.append(current_list)
output.append(lists[-1])

print(output)