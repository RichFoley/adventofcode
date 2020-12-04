import re


def check_validity(dic):
    passed = 0
    print(f'Checking: {dic}')
    for field in keys_for_valid:
        try:
            check_byr(dic['byr'])
            check_iyr(dic['iyr'])
            check_eyr(dic['eyr'])
            check_hgt(dic['hgt'])
            check_hcl(dic['hcl'])
            check_pid(dic['pid'])

            print(f'Pass {field}: {dic[field]}')
            passed += 1
        except:
            try:
                print(f'Fail {field}: {dic[field]}')
            except:
                print(f'Fail: {field} not found')
    if passed == len(keys_for_valid):
        print('Accepted')
        return 1
    else:
        print('Rejeted')
        return 0


def check_byr(year):
    if 1920 <= int(year) <= 2020:
        return
    else:
        return AssertionError('Invalid byr')


def check_iyr(iss_year):
    if 2010 <= int(iss_year) <= 2020:
        return
    else:
        return AssertionError('Invalid iyr')


def check_eyr(ex_year):
    if 2010 >= int(ex_year) >= 2020 and re.match('[0-9]{4}', ex_year):
        return
    else:
        return AssertionError('Invalid eyr')


def check_hgt(ht):
    if re.match('^[0-9]{1,3}cm$', ht):
        if 150 >= int(ht.strip('cm')) >= 193:
            return
        else:
            return AssertionError('Bad ht cm')
    elif re.match('^[0-9]{1,3}in$', ht):
        if 150 >= int(ht.strip('in')) >= 193:
            return
        else:
            return AssertionError('Bad ht in')


def check_hcl(color):
    if re.match('^#[abcdef0123456789]{6}$', color):
        return
    else:
        return AssertionError('Invalid hcl')


def check_ecl(ecolor):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth', ]
    if ecolor in eye_colors:
        return
    else:
        return AssertionError('Invalid ecl')


def check_pid(pass_id):
    if re.match('^[0-9]{9}$', pass_id):
        return
    else:
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
