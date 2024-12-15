
        #LEFT   DOWN   RIGHT   UP
dirs = [[-1,0], [0,1], [1,0], [0,-1]]
dirs_map = {'^':3, '>':2, 'v':1, '<':0, '[':2, ']':0}

def draw_map(map, width, height):                    
    line = '#'
    for i in range(width):
        line += str(i%10)
    print(line)
    for y in range(height):
        line = str(y%10)
        for x in range(width):
            line += map[(x,y)]
        print(line)
        
def calc_gps(map, width, height):
    crates = ['O', '[']
    result = 0
    for y in range(height):
        for x in range(width):
            if map[(x,y)] in crates:
                result += (100*y)+x
    return result 

def make_move(dir, obj, map):
    new_obj = (obj[0] + dirs[dir][0], obj[1]+ dirs[dir][1])
    map[new_obj] = map[tuple(obj)]
    map[tuple(obj)] = '.'

def solve_part_1(file_name, print_output = False):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        maze, moves = file.read().split('\n\n')
        map = {}
        robot = [0,0]
        width = 0
        height = 0
        for y, line in enumerate(maze.split()):
            width = len(line.strip())
            height += 1
            for x, letter in enumerate(line.strip()):
                map[(x,y)] = letter
                if letter == '@':
                    robot = [x,y]
        if print_output:
            draw_map(map, width, height)
        for i,move in enumerate(moves):
            if print_output:
                print(f'{i} {move}')
            if move in dirs_map:
                move_list = list(move_obj(dirs_map[move], robot, map))
                if 0 not in move_list:
                    robot = [robot[0]+dirs[dirs_map[move]][0], robot[1]+dirs[dirs_map[move]][1]]
                    while move_list:
                        current_move = move_list.pop()
                        if current_move != 1:
                            make_move(dirs_map[move], current_move, map)     
                    
                if print_output:
                    draw_map(map, width, height)
        print(calc_gps(map, width,  height))

def solve_part_2(file_name, print_output = False):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        maze, moves = file.read().split('\n\n')
        map = {}
        robot = [0,0]
        width = 0
        height = 0
        for y, line in enumerate(maze.split()):
            width = len(line.strip())*2
            height += 1
            for x, letter in enumerate(line.strip()):
                if letter == 'O':
                    map[(x*2,y)] = '['
                    map[(x*2+1,y)] = ']'
                else:
                    map[(x*2,y)] = letter
                    map[(x*2+1,y)] = letter
                if letter == '@':
                    robot = [x*2,y]
                    map[(x*2+1,y)] = '.'

        for i,move in enumerate(moves):
            if move in dirs_map:
                move_list = list(move_obj(dirs_map[move], robot, map))
                if 0 not in move_list:
                    robot = [robot[0]+dirs[dirs_map[move]][0], robot[1]+dirs[dirs_map[move]][1]]
                    move_set = []
                    for j in range(len(move_list)):
                        if move_list[-j-1] not in move_set and move_list[-j-1] != 1:
                            move_set.append(move_list[-j-1])
                            
                    while move_set:
                        current_move = move_set.pop(0)
                        make_move(dirs_map[move], current_move, map)        

                if print_output:
                    print(f'{i} {move}')
                    draw_map(map, width, height)
                    print('---')
        
        print(calc_gps(map, width,  height))

def move_obj(dir, obj, map):
    obj = tuple(obj)
    obj_next = (obj[0] + dirs[dir][0], obj[1]+ dirs[dir][1])

    if map[obj] == '#':
        yield 0     
        
    elif map[obj] == '.':
        yield 1
        
    elif map[obj] == '@' or map[obj] == 'O':
        yield obj
        yield from move_obj(dir, obj_next, map)
    
    else: ### part 2
        obj_pair = (obj[0] + dirs[dirs_map[map[obj]]][0], obj[1]+ dirs[dirs_map[map[obj]]][1])
        yield obj
        yield obj_pair
        obj_pair_next = (obj_pair[0] + dirs[dir][0], obj_pair[1]+ dirs[dir][1])
        if dir%2 == 1: ## if dir is vertical
            yield from move_obj(dir, obj_next, map)
        yield from move_obj(dir, obj_pair_next, map)
        

def main():
    #solve_part_1('test2.txt')
    #solve_part_1('test.txt')
    solve_part_1('data.txt', False)
    #solve_part_2('test3.txt', True)
    #solve_part_2('test.txt', True)
    solve_part_2('data.txt', False)


if __name__ == "__main__":
    main()