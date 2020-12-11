from collections import Counter


def get_file(input_file=r'd10input.txt'):
    with open(input_file) as file:
        adapters = []
        for line in file:
            val = line.strip('\n')
            adapters.append(int(val))
    return adapters


adapters = get_file()
adapters = sorted(adapters)
device = max(adapters) + 3
adapters.append(device)

differences = [x - y for x, y in zip(adapters, [0] + adapters)]
count_diffs = Counter(differences)
print(f'Count of differences: {count_diffs}')
print(f'Pt1, count of 1 diffs * 3 diffs {count_diffs[1] * count_diffs[3]}')
