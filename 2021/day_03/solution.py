def get_file(input_file=r'data.txt'):
    with open(input_file) as file:
        data = []
        for line in file:
            val = line.strip('\n')
            data.append(bytes(val, 'ascii'))
    return data


bin_output = get_file()
print(bin_output)


def extract_bits(bits_list, pos):
    for bit_str in bits_list:



def count_bits(bit_list):
    pass