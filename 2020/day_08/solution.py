
def get_file(input_file=r'd8input.txt'):
    with open(input_file) as file:
        instructions_dict = {}
        for idx, line in enumerate(file):
            inst, val = line.split()
            instructions_dict[idx] = {'inst': inst,
                                 'val': float(val),
                                 'used': None}
    return instructions_dict


def move(row=0, acc=float(0)):
    if row == len(instructions):
        print(f'Success: acc was at: {acc}')
    else:
        if instructions[row]['used']:
            pass
        else:
            if instructions[row]['inst'] == 'nop':
                instructions[row]['used'] = True
                row += 1
                move(row, acc)
            elif instructions[row]['inst'] == 'jmp':
                instructions[row]['used'] = True
                row += instructions[row]['val']
                move(row, acc)
            elif instructions[row]['inst'] == 'acc':
                instructions[row]['used'] = True
                acc += instructions[row]['val']
                row += 1
                move(row, acc)


instructions = get_file()
move()

for idx in range(0, len(instructions)):
    print(f'Swapping: {idx}')
    if instructions[idx]['inst'] == 'nop':
        instructions[idx]['inst'] = 'jmp'
        move()
        instructions = get_file()
    elif instructions[idx]['inst'] == 'jmp':
        instructions[idx]['inst'] = 'nop'
        move()
        instructions = get_file()



