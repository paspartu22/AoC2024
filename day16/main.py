from queue import PriorityQueue

        #UP     RIGHT   DOWN   LEFT         
dirs = [[0,-1], [1,0],  [0,1], [-1,0]]
dirs_image = ['^', '>', 'v', '<']

width = 0
height = 0

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        global width
        global height
        height = 0
        print(f'{file_name} part 1')
        map = {}
        start = (0, 0)
        finish = (0,0)

        for y, line in enumerate(file.read().splitlines()):
            width = len(line.strip())
            height += 1
            for x, letter in enumerate(line.strip()):
                if letter != '#':
                    map[x, y] = (x,y)
                if letter == 'S':
                    start = (x, y)
                if letter == 'E':
                    finish = (x, y)
        print(bfs(map, start, finish))
        
def bfs(map, start, finish):
    pq = PriorityQueue()
    pq.put((0, start, 1))
    visited = {(start, 1) : 0}
    while pq.qsize() > 0:
        current_pos = pq.get()
        #print (current_pos)
        for i,dir in enumerate(dirs):
            new_cell = (current_pos[1][0] + dir[0], current_pos[1][1] + dir[1])
            if new_cell in map and abs(i-current_pos[2]) != 2:
                distance = current_pos[0] + (i-current_pos[2])%2*1000 + 1
                if distance == 10033:
                    pass
                if (new_cell, i) not in visited or visited[(new_cell, i)] >= distance:
                    pq.put((distance, new_cell, i))
                    visited[(new_cell, i)] = distance
                    #print_map(map, visited, current_pos, new_cell, finish)
                    #print(distance)    
                    if new_cell == finish:
                        path = set(get_path(visited, (finish,i)))
                        #print_map(map, visited, current_pos, new_cell, path)
                        print(len(path))
                        return visited[finish, i]

def get_path(visited, finish):
    queue = [finish]
    path = [finish[0]]
    while len(queue) > 0:
        current_pos = queue.pop()
        for i,dir_input in enumerate(dirs):
            new_cell = (current_pos[0][0] + dir_input[0], current_pos[0][1] + dir_input[1])
            for j,dir_output in enumerate(dirs):
                if ((i+2)%4 == j and (new_cell,j) in visited and visited[current_pos] - visited[(new_cell,j)] == 1):
                    path.append(new_cell)
                    queue.append((new_cell, j))
                if ((i+j)%2 == 1 and (new_cell,j) in visited and visited[current_pos] - visited[(new_cell,j)] == 1001):
                    path.append(new_cell)
                    queue.append((new_cell, j))
    return path

def print_map(map, visited, current_position, new_cell, path = []):
    global width
    global height
    start = "\033[1m"
    end = "\033[0;0m"
    line = '#'

    for i in range(width):
        line += str(i%10)
    print(line)
    for y in range(height):
        line = str(y%10)
        for x in range(width):
            if (x,y) not in map:
                line += ' '
            elif (x, y) == current_position[1]:
                line += dirs_image[current_position[2]]
            else:
                if (x,y) in path:
                    line += '*'
                else:
                        
                    add = 999999
                    for i in range(4):
                        if ((x,y), i) in visited:
                            add = min(add, visited[(x,y),i])
                    if add == 999999:
                        add = '.'
                    elif add < 1000:
                        add = str(add)[-1]
                    else: 
                        add = str(add)[-4]
                    line += start + str(add) + end if (x,y) == tuple(new_cell) else str(add) 
        print(line)

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')

def main():
    solve_part_1('test.txt')
    print(f'result 7036')
    solve_part_1('test2.txt')
    print(f'result 11048')
    solve_part_1('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')

if __name__ == "__main__":
    main()