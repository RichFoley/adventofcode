input_ls = []

with open('input.txt') as file:
    for line in file:
        line = line.split()
        input_ls.append(line)

print(input_ls)

sample_ls = [[7, 6, 4, 2, 1],
             [1, 2, 7, 8, 9],
             [9, 7, 6, 2, 1],
             [1, 3, 2, 4, 5],
             [8, 6, 4, 4, 1],
             [1, 3, 6, 7, 9]
             ]

def report_safe(report_ls):
    #Check if all increasing or decreasing
    all_inc = None
    all_dec = None
    for x in report_ls:
