boarding_passes = []
results = []
columns = 8

with open('d5input.txt') as file:
    for line in file:
        line = line.strip('\n')
        line = [line[:7], line[7:]]
        boarding_passes.append(line)

for bpass in boarding_passes:
    row = []
    num = 0
    for n in range(0, 127 + 1):
        row.append(num)
        num += 1
    print(bpass[0])
    for char in bpass[0]:
        print(char)
        if char == 'F':
            row = row[:int(len(row)/2)]
        if char == 'B':
            row = row[int(len(row)/2):]
        print(row)

    column = []
    num = 0
    for n in range(0, 7 + 1):
        column.append(num)
        num += 1
    print(bpass[1])
    for char in bpass[1]:
        print(char)
        if char == 'L':
            column = column[:int(len(column) / 2)]
        if char == 'R':
            column = column[int(len(column) / 2):]
        print(column)
    results.append([*row, *column])

print(results)

seat_ids = []
for result in results:
    seat_ids.append(result[0] * 8 + result[1])

print(seat_ids)
print(max(seat_ids))

# Generate all possible
all_ids = []
row = []
num = 0
for n in range(0, 127 + 1):
    row.append(num)
    num += 1

column = []
num = 0
for n in range(0, 7 + 1):
    column.append(num)
    num += 1
print(row)
print(column)

for ro in row:
    for col in column:
        all_ids.append(ro * col)

all_ids = list(dict.fromkeys(all_ids))
print(all_ids)

print(list(set(all_ids) - set(seat_ids)))
