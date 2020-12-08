import re

rules = []
with open('d7input.txt') as file:
    for line in file:
        line = line.strip('\n')
        line = re.split(r' bags contain | bags?.? ?', line)
        line = list(filter(None, line))
        rule_set = []
        for idx, item in enumerate(line):
            if idx > 0:
                if item != 'no other':
                    rule = ([item[2:], item[0]])
                    rule_set.append(rule)
            else:
                rule = [item, 1]
                rule_set.append(rule)
        rule_set.reverse()
        rules.append(rule_set)
    print(rules)

# matches = []
# last_search_term = ''
#
#
# def search(rule_list, search_term):
#     filtered_rules = []
#     global last_search_term
#
#     for rule_set in rule_list:
#         for idx, rule in enumerate(rule_set):
#
#             matches.append(search_term)
#             if search_term != last_search_term and search_term in rule:
#                 print(f'Searching: {search_term}')
#                 last_search_term = search_term
#                 try:
#                     # matches.append(rule_set[idx+1])
#
#                     search(rule_list=rules, search_term=rule_set[idx+1][0])
#                     print(f'Added: {rule_set[idx+1]}')
#
#
#                 except:
#                     print('Top of tree')
#                 print(f'idx: {idx}')
#
#                 # print(rule_set[idx], rule_set[idx+1])
#                 # search(rule_list=rules, search_term=item[len][0])
#
#     print(filtered_rules)
#     print(list(dict.fromkeys(matches)))
#     print(f'Bags: {len(list(dict.fromkeys(matches)))-1}')
#
#
# search(rule_list=rules, search_term='shiny gold')
search_term = 'shiny gold'


def find_bag(rules, search_term):
    filtered_rules = []
    for rule_set in rules:
        for rule in rule_set:
            if search_term in rule:
                filtered_rules.append(rule_set)
    return filtered_rules


def find_parents(rules, filtered_rules):
    parent_search = []
    for rule_set in filtered_rules:
        for idx, rule in enumerate(rule_set):
          if rule[0] == search_term:
              parent_search.append(rule_set[idx:])

    for parent_set in parent_search:
        for idx, rule in enumerate(parent_set):
            find_bag(rules, rule[0])
        for rule_set in rules:
            pass


filtered_rules = find_bag(rules=rules, search_term=search_term)

print(filtered_rules)

print(find_parents(rules=rules, filtered_rules=filtered_rules))