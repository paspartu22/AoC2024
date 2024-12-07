#import sys
#from time import sleep

dirs = [[-1,0], [0,1], [1,0], [0,-1]]





def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        width = 0
        height = 0
        current_pos = []
        map = {}
        print(f'{file_name} part 1')
        for y, line in enumerate(file.readlines()):
            width = len(line.strip())
            height += 1
            for x, item in enumerate(line.strip()):
                if item == '#':
                    map[y, x] = '#'
                else:
                    map[y, x] = '.'
                if item == '^':
                    current_pos = (y, x)
        result = 0


        part1_visited = set([item[0] for item in check_map(map, current_pos, width, height)])
        print(len(part1_visited))
        draw_map(map, width, height, part1_visited)
        for y in range(height):
            for x in range(width):
                if map[y, x] == '.' and (y, x) != current_pos and (y,x) in part1_visited:
                    new_map = map.copy()
                    new_map[y, x] = '#'
                    if (check_map(new_map, current_pos, width, height) == 1):
                        result += 1
                        print((y, x), flush = True)
        print()
        print(result)
        
def check_map(map, current_pos, width, height):
    current_dir = 0
    visited = []
    while(1):
        next_move = get_next_move(current_pos, current_dir) 

        if  next_move not in map:
            visited.append((current_pos, current_dir))
            return set(visited)
        
        elif (current_pos, current_dir) in visited:
            #draw_map(map, width, height, visited)
            return 1
        else:
            visited.append((current_pos, current_dir))

        if map[next_move] == '.':
            current_pos = next_move
        elif map[next_move] == '#':
            current_dir = (current_dir + 1) % 4
        
        else:
            print('wtf')
            
        
        #sys.stdout.flush()
        
        #print("\033[%d;%dH" % (current_pos))
        #print('x', end='')
        #sleep(0.05)

    #print(current_pos)
    #print(len(set(visited)))
    #draw_map(map, width, height, visited)

def get_next_move(current_pos, current_dir):
    return (current_pos[0]+dirs[current_dir][0], current_pos[1]+dirs[current_dir][1])

def draw_map(map, width, height, visited):
    for y in range(height):            
        line = ""
        for x in range(width):
            if (y, x) in visited:
                line += 'x'
            elif map[y, x] == '#':
                line += '#'
            else:
                line += 'o'
        print(line)
    

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