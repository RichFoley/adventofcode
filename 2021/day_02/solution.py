import re


def get_file(input_file=r'data.txt'):
    with open(input_file) as file:
        data = []
        for line in file:
            val = line.strip('\n')
            data.append(val)
    return data


raw_commands = get_file()
commands = []

for raw_command in raw_commands:
    split_tpl = re.match('^([a-z]\w+)(?:.)(\d+)$', raw_command).groups()
    to_list = [split_tpl[0], int(split_tpl[1])]
    commands.append(to_list)
print(commands)

depth = 0
dist = 0

for command in commands:
    if command[0] == 'up':
        depth -= command[1]
    elif command[0] == 'down':
        depth += command[1]
    elif command[0] == 'forward':
        dist += command[1]

print(f'Travelled {dist} and reached depth of {depth}.')
print(f'Depth * Dist = {depth * dist}')

# Part Two

depth = 0
dist = 0
aim = 0
for command in commands:
    if command[0] == 'up':
        aim -= command[1]
    elif command[0] == 'down':
        aim += command[1]
    elif command[0] == 'forward':
        dist += command[1]
        depth += aim * command[1]

print(f'Travelled {dist} and reached depth of {depth}. Aim of {aim}')
print(f'Depth * Dist = {depth * dist}')