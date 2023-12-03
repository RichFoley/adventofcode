import re


def get_file(input_file=r'input.txt'):
    with open(input_file) as file:
        data = []
        for line in file:
            val = line.strip('\n')
            data.append(val)
    return data


def replace_all(text, di):
    for i, j in di.items():
        text = text.replace(i, j)
    return text


# because some words overlap...
txt_2_num = {
    'one':   'on1ne',
    'two':   'tw2wo',
    'three': 'thr3ree',
    'four':  'fou4our',
    'five':  'fiv5ive',
    'six':   'si6ix',
    'seven': 'sev7ven',
    'eight': 'eig8ght',
    'nine':  'nin9ine'
}

input_ls = get_file()
numbers_ls = []
flat_numbers_ls = []
final_numbers_ls = []

for line in input_ls:

    new_line = replace_all(line, txt_2_num)
    numbers_ls.append(re.findall(r'\d+', new_line))

for numls in numbers_ls:
    concatted_digits = ''
    for num in numls:
        concatted_digits = concatted_digits + str(num)
    flat_numbers_ls.append(concatted_digits)

for num in flat_numbers_ls:
    final_numbers_ls.append(int(num[0]+num[-1]))


sum_nums = sum(final_numbers_ls)

print(input_ls)
print(numbers_ls)
print(flat_numbers_ls)
print(final_numbers_ls)
print(f'Sum of all numbers is {sum_nums}.')
