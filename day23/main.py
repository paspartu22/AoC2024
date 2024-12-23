from collections import defaultdict
from itertools import combinations

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        map = defaultdict(list)
        for line in file.read().splitlines():
            a,b = line.split('-')
            map[a].append(b)
            map[b].append(a)
        for item in map.items():
            print(item)

        parties = set()
        for user_1 in map.items():
            for user_2 in user_1[1]:
                for user_3 in map[user_2]:
                    if user_1[0] in map[user_3]:
                        parties.add(tuple(sorted((user_1[0], user_2, user_3))))
        print(len(parties))
        result = 0
        for party in parties:
            if any([True for p in party if p[0] == 't']):
                result += 1
        print(result)


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