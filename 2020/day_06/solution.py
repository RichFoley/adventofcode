groups = []
group = []
with open('d6input.txt') as file:
    for line in file:
        if line != '\n':
            line = line.strip('\n')
            group.extend([char for char in line])
        else:
            groups.append(group)
            group = []
print(groups)

groups = [set(group) for group in groups]
print(groups)

g_totals = [len(group) for group in groups]

print(f'Total anyone answered: {sum(g_totals)}')

# Pt 2

groups = []
group = []
with open('d6input.txt') as file:
    for line in file:
        if line != '\n':
            line = line.strip('\n')
            group.append([char for char in line])
        else:
            groups.append(group)
            group = []
print(groups)

argeements = []
for group in groups:
    if len(group) > 1:
        argeements.append(set.intersection(*[set(person) for person in group]))
    else:
        argeements.append(set(*group))

print(argeements)
print([len(group) for group in argeements])

g_totals = [len(group) for group in argeements]

print(f'Total all answered: {sum(g_totals)}')
