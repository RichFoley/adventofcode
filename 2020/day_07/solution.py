import re
from collections import OrderedDict

rules = []
with open('sample_input.txt') as file:
    for line in file:
        line = line.strip('\n')
        line = re.split(r' bags contain | bags?.? ?', line)
        line = list(filter(None, line))
        line_dict = OrderedDict()
        for idx, item in enumerate(line):
            if idx > 0:
                key = item[2:]
                value = item[0]
            else:
                key = item
                value = 1
            line_dict[key] = value
        print(line_dict)
        print(line)

