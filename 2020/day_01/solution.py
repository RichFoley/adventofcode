with open(file=r'd1input.txt') as file:
    entries = file.readlines()

entries = [entry.strip('\n') for entry in entries]
print(f'Inputs: {entries}')

add_for_2020 = []

# Ugly triple-nested for loop garbage code:
for entry1 in entries:
    for entry2 in entries:
        for entry3 in entries:
            sumrslt = int(entry1) + int(entry2) + int(entry3)
            if sumrslt == 2020:
                add_for_2020.append([entry1, entry2, entry3])

solution = []
for set_of_summed in add_for_2020:
    solution.append(int(set_of_summed[0]) * int(set_of_summed[1]) * int(set_of_summed[2]))

print(f'Solution = {solution[0]}')
