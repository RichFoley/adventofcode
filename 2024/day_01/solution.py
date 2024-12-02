input_ls = []

with open('input.txt') as file:
    for line in file:
        line = line.split()
        input_ls.append(line)

list_1 = []
list_2 = []
for num_pair in input_ls:
    list_1.append(num_pair[0])
    list_2.append(num_pair[1])


print(list_1)
list_1 = list(map(int, list_1))
list_2 = list(map(int, list_2))

list_1.sort()
list_2.sort()
print(list_1)
print(list_2)

diff_ls = []
for l1x, l2x in zip(list_1, list_2):
    diff_ls.append(l2x-l1x)
print(diff_ls)
diff_ls = list(map(abs, diff_ls))
print(diff_ls)
summed = sum(diff_ls)
print(summed)

similarity_set_ls = []

for l1_num in list_1:
    match_count = 0
    for l2_num in list_2:
        match_count += 1 if l1_num == l2_num else 0

    similarity_set_ls.append([l1_num, match_count])

simil_ls = []
for match_set in similarity_set_ls:
    simil_ls.append(match_set[0] * match_set[1])

print(sum(simil_ls))