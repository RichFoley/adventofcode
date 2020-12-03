# https://adventofcode.com/2020/day/3
from functools import reduce

with open(file=r'd3input.txt') as file:
    inputs = file.readlines()
inputs = [line.strip('\n') for line in inputs]

print('Starting Map:')
for line in inputs:
    print(line)

slopes = [
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 1},
    {'x': 5, 'y': 1},
    {'x': 7, 'y': 1},
    {'x': 1, 'y': 2},
]
# (From top left)


def mark_trees(coords, current_line):
    current_line = list(current_line)
    if current_line[coords['x']] == '#':
        current_line[coords['x']] = 'X'
    else:
        current_line[coords['x']] = 'O'
    return ''.join(current_line)


def check_slope(slope):
    pointer = {'x': 0, 'y': 0}
    print(f'Slope: {slope}')
    output_map = []

    for idx, line in enumerate(inputs):
        if idx == pointer['y']:

            mkd_line = mark_trees(pointer, line)
            output_map.append(mkd_line)

            # Index pointer
            pointer['x'] = pointer['x'] + slope['x']
            if pointer['x'] > (len(line)-1):
                pointer['x'] = pointer['x'] - (len(line))
            pointer['y'] = pointer['y'] + slope['y']

        else:
            output_map.append(line)
    return output_map


def count_trees(marked_map):

    trees = 0
    for line in marked_map:
        trees = trees + line.count('X')
        print(line)
    print(f'We hit {trees} trees!')
    return trees


results = []
for slo in slopes:
    results.append(count_trees(check_slope(slo)))

print(results)
product = reduce((lambda x, y: x * y), results)
print(f'Product = {product}')