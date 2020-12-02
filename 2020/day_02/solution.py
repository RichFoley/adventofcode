import re
with open(file=r'd2input.txt') as file:
    inputs = file.readlines()

inputs = [entry.strip('\n') for entry in inputs]
inputs = [entry.split() for entry in inputs]
print(f'Inputs: {inputs}')

valid_lines = []
for line in inputs:
    char_count = line[0].replace('-', ',')
    match_char = line[1].strip(':')
    password = line[2]
    regex_patt = f'([{match_char}]{{1}}){{{char_count}}}'

    if re.fullmatch(pattern=regex_patt, string=password):
        valid_lines.append([password, line])

print(valid_lines)