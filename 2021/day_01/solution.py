def get_file(input_file=r'data.txt'):
    with open(input_file) as file:
        data = []
        for line in file:
            val = line.strip('\n')
            data.append(int(val))
    return data


depths = get_file()
count_increases = 0

for i in range(len(depths)):
    if i == 0:
        increases = None
    elif depths[i] > depths[i-1]:
        increases = True
        count_increases += 1
    else:
        increases = False

print(f'{count_increases} values increase')

# Part two
count_increases = 0
windows = []
for i in range(len(depths)):
    if 1 < i <= len(depths):
        windows.append(depths[i]+depths[i-1]+depths[i-2])

for i in range(len(windows)):
    if i == 0:
        increases = None
    elif windows[i] > windows[i-1]:
        increases = True
        count_increases += 1
    else:
        increases = False

print(f'{count_increases} windows increase')
