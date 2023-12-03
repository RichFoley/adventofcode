import re


def get_file(input_file=r'input.txt'):
    with open(input_file) as file:
        data = []
        for line in file:
            val = line.strip('\n')
            data.append(val)
    return data


games_ls = get_file()
game_dicts = []

print(games_ls[0].split(':'))
for line in games_ls:
    game = line.split(':')[0]
    game_no = int(re.findall(r'\d+', game)[0])

    results = line.split(':')[1].split(';')


