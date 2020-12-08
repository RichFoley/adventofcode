import pandas as pd
import re
# input_file = r'sample_input.txt'


def get_file(input_file=r'd8input.txt'):
    with open(input_file) as file:
        instructions_dict = {}
        for idx, line in enumerate(file):
            inst, val = line.split()
            instructions_dict[idx] = {'inst': inst,
                                 'val': float(val),
                                 'used': None}
    #print(instructions_dict)
    return instructions_dict


instructions = get_file()


def move(row=0, acc=float(0)):
    if row == len(instructions):
        print(f'Success: acc was at: {acc}')
    else:
        if instructions[row]['used']:
            pass
            #print(f'Infinity! acc was at: {acc}')
        else:
            if instructions[row]['inst'] == 'nop':
                instructions[row]['used'] = True
                # print(f'Row: {row}, {instructions[row]["inst"]}, {acc}')
                row += 1
                move(row, acc)
            elif instructions[row]['inst'] == 'jmp':
                instructions[row]['used'] = True
                # print(f'Row: {row}, {instructions[row]["inst"]}, {acc}')
                row += instructions[row]['val']
                move(row, acc)
            elif instructions[row]['inst'] == 'acc':
                instructions[row]['used'] = True
                acc += instructions[row]['val']
                # print(f'Row: {row}, {instructions[row]["inst"]}, Val:{instructions[row]["val"]} {acc}')
                row += 1
                move(row, acc)


move()

#print(instructions)
for idx in range(0, len(instructions)):
    print(f'Swapping: {idx}')
    if instructions[idx]['inst'] == 'nop':
        instructions[idx]['inst'] = 'jmp'
        #print(instructions)
        move()
        instructions = get_file()
    elif instructions[idx]['inst'] == 'jmp':
        instructions[idx]['inst'] = 'nop'
        #print(instructions)
        move()
        instructions = get_file()



