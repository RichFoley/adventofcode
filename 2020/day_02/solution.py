import re
with open(file=r'd2input.txt') as file:
    inputs = file.readlines()

inputs = [entry.strip('\n') for entry in inputs]
inputs = [entry.split() for entry in inputs]
print(f'Inputs: {inputs}')

valid_lines = []
for line in inputs:
    char_count = line[0].split('-')
    match_char = line[1].strip(':')
    password = line[2]
    regex_patt = f'([{match_char}]{{1}}){{{char_count}}}'
    matches = password.count(match_char)
    if int(char_count[0]) <= matches <= int(char_count[1]):
        valid_lines.append([password, line])

print(valid_lines)
print('Part one:')
print(f'{len(valid_lines)} of {len(inputs)} passwords are valid')

valid_lines = []
for line in inputs:
    index1, index2 = line[0].split('-')
    match_char = line[1].strip(':')
    password = line[2]
    if (password[int(index1)-1] == match_char and password[int(index2)-1] != match_char) \
            or (password[int(index1)-1] != match_char and password[int(index2)-1] == match_char):
        valid_lines.append([password, line])

print(valid_lines)
print('Part two:')
print(f'{len(valid_lines)} of {len(inputs)} passwords are valid')