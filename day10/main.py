dirs = [(0,-1),(1,0),(0,1),(-1,0)]

def solve_part_1(file_name):
    cells = {}
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        for y,line in enumerate(file.read().splitlines()):
            for x, number in enumerate(line):
                cells[(x, y)] = int(number)
        result1 = 0
        result2 = 0
        for cell in cells:
            if cells[cell] == 0:
                result = list(dfs(cells, cell))
                result2 += len(result)
                result1 += len(set(result))
        print(result1)
        print(result2)

def dfs(cells, cell):
    if (cells[cell]) == 9:
        yield cell
    
    for dir in dirs:
        new_cell = (cell[0] + dir[0], cell[1] + dir[1])
        if new_cell in cells and cells[new_cell] - 1 == cells[cell]:
            yield from dfs(cells, new_cell)


def main():
    solve_part_1('test.txt')
    solve_part_1('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()