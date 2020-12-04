import re


def check_validity(dic):
    passed = 0
    print(f'Checking: {dic}')

    try:
        passed = passed + check_byr(dic['byr'])
        passed = passed + check_iyr(dic['iyr'])
        passed = passed + check_eyr(dic['eyr'])
        passed = passed + check_hgt(dic['hgt'])
        passed = passed + check_hcl(dic['hcl'])
        passed = passed + check_ecl(dic['ecl'])
        passed = passed + check_pid(dic['pid'])

        print(f'Pass: {dic}')
    except:
        try:
            print(f'Fail:{dic}')
        except:
            print(f'Fail: {dic} field not found')
    print(f'{passed} of {len(keys_for_valid)} passed')
    if passed == len(keys_for_valid):
        print('Accepted')
        return 1
    else:
        print('Rejeted')
        return 0


def check_byr(year):
    if 1920 <= int(year) <= 2002:
        print('Pass: byr')
        return 1
    else:
        print('Fail: byr')
        return AssertionError('Invalid byr')


def check_iyr(iss_year):
    if 2010 <= int(iss_year) <= 2020:
        print('Pass: iyr')
        return 1
    else:
        print('Fail: byr')
        return AssertionError('Invalid iyr')


def check_eyr(ex_year):
    if 2020 <= int(ex_year) <= 2030:
        print('Pass: eyr')
        return 1
    else:
        print('Fail: eyr')
        return AssertionError('Invalid eyr')


def check_hgt(ht):
    if re.match('^[0-9]{1,3}cm$', ht):
        if 150 <= int(ht.strip('cm')) <= 193:
            print('Pass: htcm')
            return 1
        else:
            print(f'Fail: htcm:{int(ht.strip("cm"))}')
            return AssertionError('Bad ht cm')
    elif re.match('^[0-9]{1,3}in$', ht):
        if 59 <= int(ht.strip('in')) <= 76:
            print('Pass: htin')
            return 1
        else:
            print('Fail: htin')
            return AssertionError('Bad ht in')
    else:
        return AssertionError('No unit')


def check_hcl(color):
    if re.match('^#[abcdef0123456789]{6}$', color):
        print('Pass: hcl')
        return 1
    else:
        print('Fail: hcl')
        return AssertionError('Invalid hcl')


def check_ecl(ecolor):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth', ]
    if ecolor in eye_colors:
        print('Pass: ecl')
        return 1
    else:
        print('Fail: ecl')
        return AssertionError('Invalid ecl')


def check_pid(pass_id):
    if re.match('^[0-9]{9}$', pass_id):
        print('Pass: pid')
        return 1
    else:
        print('Fail: pid')
        return AssertionError('Invalid pid')


keys_for_valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = []
passport = []
with open('d3input.txt') as file:
    for line in file:
        if line != '\n':
            line = line.strip('\n').split(' ')
            passport.append(line)
        else:
            passport = [item for sublist in passport for item in sublist]
            passport_dict = {}
            for key_value in passport:
                key, value = key_value.split(':', 1)
                passport_dict[key] = value
            passports.append(passport_dict)
            passport = []
print(passports)
valid = 0
for passport in passports:
    valid = valid + check_validity(passport)



print(f'{valid} are valid')
