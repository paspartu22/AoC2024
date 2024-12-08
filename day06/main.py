import time
import threading
import os

dirs = [[-1,0], [0,1], [1,0], [0,-1]]
result = 0
        
def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        global result
        result = 0
        width = 0
        height = 0
        current_pos = []
        map = {}
        walls = []
        print(f'{file_name} part 1')
        for y, line in enumerate(file.readlines()):
            width = len(line.strip())
            height += 1
            for x, item in enumerate(line.strip()):
                if item == '#':
                    map[y, x] = '#'
                    walls.append((y,x))
                else:
                    map[y, x] = '.'
                if item == '^':
                    current_pos = (y, x)



        part1_visited = set([item[0] for item in check_map(current_pos, width, height, walls, True)])
        print(len(part1_visited))
        # walls.append((0,0))
        #draw_map(map, width, height, part1_visited)
        threads = {}
        for y,x in part1_visited:
            if (y,x) != current_pos:
                new_walls = walls.copy()
                new_walls.append((y,x))
                threads[y,x] = threading.Thread(target = check_map, args = (current_pos, width, height, new_walls))
                threads[y,x].start()

        for thread in threads.values():
            thread.join()
        print()
        print(result)
        
def check_map(current_pos, width, height, walls, part1 = False):
    current_dir = 0
    visited = []
    global result
    while(1):
        next_move = list(map(sum(current_pos, dirs[current_dir]))) 

        if  next_move[0] < 0 or next_move[0] > height or next_move[1] < 0 or next_move[1] > width:
            return visited if part1 else 0
        
        elif (current_pos, current_dir) in visited:
            result += 1
            print(result)
            return 1
        elif (part1):
            visited.append((current_pos, current_dir))

        if next_move not in walls:
            current_pos = next_move
        else:
            visited.append((current_pos, current_dir))
            current_dir = (current_dir + 1) % 4
        


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
    


def main():
    start = time.time()
    solve_part_1(f'{os.path.dirname(__file__)}/test.txt')
    solve_part_1(f'{os.path.dirname(__file__)}/data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')
    end = time.time()
    input(f'Time elapced {end - start}')


if __name__ == "__main__":
    main()