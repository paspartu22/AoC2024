dirs = [(0,-1),(1,0),(0,1),(-1,0)]

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        map = {}
        for y, line in enumerate(file.read().splitlines()):
            for x, letter in enumerate(line):
                map[x, y] = {'letter' : letter, 'visited' : 0, 'fence':[0,0,0,0]}

        result = 0
        for plot in map.items():
            if plot[1]['visited'] == 0 :
                area, perimeter = dfs(map, plot[0])
                result += (area*perimeter)
                #print(f'{area} {perimeter}')
        print (result)

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        map = {}
        for y, line in enumerate(file.read().splitlines()):
            for x, letter in enumerate(line):
                map[x, y] = {'letter' : letter, 'visited' : 0, 'fence':[0,0,0,0]}

        result = 0        
        for plot in map.items():
            if plot[1]['visited'] == 0 :
                area, perimeter = dfs_part_2(map, plot[0])
                result += (area*perimeter)
                #print(f'{area} {perimeter}')
        print (result)

def dfs(map, cell):
    area = 1
    perimeter = 0
    map[cell]['visited'] = 1
    for dir in dirs:
        new_cell = (cell[0] + dir[0], cell[1] + dir[1])
        if new_cell in map and map[new_cell]['letter'] != map[cell]['letter'] or new_cell not in map:
            perimeter += 1
        elif map[new_cell]['letter']== map[cell]['letter'] and map[new_cell]['visited'] == 0:
            _area, _perimeter = dfs(map, new_cell)
            area += _area
            perimeter += _perimeter
    return (area, perimeter)

def dfs_part_2(map, cell):
    area = 1
    map[cell]['visited'] = 1
    perimeter = 0
    for i,dir in enumerate(dirs):
        new_cell = (cell[0] + dir[0], cell[1] + dir[1])
        if (map[cell]['fence'][i] == 0 and 
                (new_cell in map 
                and map[new_cell]['letter'] != map[cell]['letter'] 
                or new_cell not in map)):
            perimeter += 1
            map[cell]['fence'][i] = 1
            
            dfs_fence(map, cell, (i+1)%4, side = 'left')
            dfs_fence(map, cell, (i+3)%4, side = 'right')

        elif new_cell in map and map[new_cell]['letter']== map[cell]['letter'] and map[new_cell]['visited'] == 0:
            _area, _perimeter = dfs_part_2(map, new_cell)
            area += _area
            perimeter += _perimeter

    return (area, perimeter)

def dfs_fence(map, cell, dir, side):
    new_cell = (cell[0] + dirs[dir][0], cell[1] + dirs[dir][1])
    fence_dir = (dir+1)%4
    if side == 'left':
        fence_dir = (dir+3)%4

    new_cell_fence = (new_cell[0] + dirs[fence_dir][0], new_cell[1] + dirs[fence_dir][1]) 

    if (new_cell in map and 
        map[new_cell]['letter'] == map[cell]['letter'] and 
        (new_cell_fence in map and
        map[new_cell]['letter'] != map[new_cell_fence]['letter']
        or new_cell_fence not in map)):
        map[new_cell]['fence'][fence_dir] = 1
        dfs_fence(map, new_cell, dir, side)
    
def main():
    solve_part_1('test2.txt')
    #solve_part_1('test.txt')
    solve_part_1('data.txt')
    solve_part_2('test2.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()