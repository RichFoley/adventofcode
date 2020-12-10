
def get_file(input_file=r'd9input.txt'):
    with open(input_file) as file:
        adapters = []
        for line in file:
            val = line.strip('\n')
            adapters.append(int(val))
    return adapters



# def check_num(current_idx):
#     current_num_set = cypher[current_idx-preamble:current_idx]
#     if not sum_valid(current_num_set, cypher[current_idx]):
#         invalid = cypher[current_idx]
#     else:
#         return check_num(current_idx+1)
#     return invalid
#
#
# def sum_valid(num_set, target):
#     for num1 in num_set:
#         for num2 in num_set:
#             if num1 + num2 == target:
#                 return True
#     return False
#
#
# def test_sets(target):
#     for idx, num1 in enumerate(cypher):
#         for idy, num2 in enumerate(cypher):
#             if sum(cypher[idx:idy]) == target and len(cypher[idx:idy]) != 1:
#                 print(idx, idy)
#                 print(cypher[idx:idy])
#                 key = min(cypher[idx:idy])+max(cypher[idx:idy])
#                 print(f'Part2: enc key= {key}')
#
#
# preamble = 25
# cypher = get_file()
# invalid_num = check_num(current_idx=preamble)
# print(f'Part 1: 1st invalid number = {invalid_num}')
#
# test_sets(invalid_num)

