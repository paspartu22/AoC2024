
def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        #lines = file.read()
        #print(lines)
        rules_str, updates = file.read().split("\n\n")
        rules_str = rules_str.split('\n')
        updates = updates.split('\n')
        rules = {}
        for rule in rules_str:
            if int(rule.split('|')[0]) in rules:
                rules[int(rule.split('|')[0])].append(int(rule.split('|')[1]))
            else:
                rules[int(rule.split('|')[0])] = [int(rule.split('|')[1])]
        #for rule in rules.items():
            #print(rule)
        print('---')
        #print(updates)
        result_1 = 0
        result_2 = 0
        for update in updates:
            update = [int(item) for item in update.split(',')]
            #print(update)
            if check_update(rules, update):
                result_1 += update[len(update)//2]
            else:
                result_2 += fix_update(rules, update)
        print(result_1)
        print(result_2)

def fix_update(rules, update):
    do_again = True
    while (do_again):
        do_again = False
        for id,number in enumerate(update):
            if number in rules:
                for rule in rules[number]:
                    if rule in update and id > update.index(rule):
                        do_again = True
                        update[id], update[update.index(rule)] = update[update.index(rule)], update[id]
    #print(update)
    return update[len(update)//2]
    # return 1

def check_update(rules, update):
    for id,number in enumerate(update):
        if number in rules:
            for rule in rules[number]:
                if rule in update and id > update.index(rule):
                    return 0
    return 1

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')


def main():
    solve_part_1('test.txt')
    solve_part_1('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()