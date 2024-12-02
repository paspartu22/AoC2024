UP = 0
DOWN = 1
valid = [[1, 2, 3], [-1, -2, -3]]


def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')


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