
        #UP     RIGHT   DOWN   LEFT         
dirs = [[0,-1], [1,0],  [0,1], [-1,0]]

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        map = []
        start = (0,0)
        end = (0,0)
        width = 0
        height = 0
        for y, line in enumerate(file.read().splitlines()):
            for x, letter in enumerate(line.strip()):
                if letter != '#':
                    map.append((x,y))
                if letter == 'S':
                    start = (x,y)
                if letter == 'E':
                    end = (x,y)
        width = x
        height = y

        len_from_start = bfs(map, start, end)
        basic_len = len_from_start[end]
        print(basic_len)
        #print_path(map, len_from_start, width, height)
        len_from_end = bfs(map, end, start)
        cuts = []
        for y in range(height):
            for x in range(width):
                if (x,y) not in map:
                    if ((x+1,y) in map and (x-1,y) in map):
                        cuts.append((x,y,check_cut(len_from_start[(x+1,y)],len_from_start[(x-1,y)], len_from_end[(x+1,y)],len_from_end[(x-1,y)], basic_len)))
                    elif (x,y+1) in map and (x,y-1) in map:
                        cuts.append((x,y,check_cut(len_from_start[(x,y+1)],len_from_start[(x,y-1)], len_from_end[(x,y+1)],len_from_end[(x,y-1)], basic_len)))
        #for cut in cuts:
            #print(cut)
        result = 0
        #print('----------')
        cuts_list = {}
        for cut in cuts:
            if cut[-1] >= 100:
                result += 1
            if cut[-1] in cuts_list:
                cuts_list[cut[-1]] += 1
            else:
                cuts_list[cut[-1]] = 1
        #for cut in cuts_list.items():
           # print(cut)
        print(result)
#        print(cuts_list)
        #path = get_path(visited, end, start)
        #print_path(map, path, y, x)
        #print(len)

def check_cut(s_left, s_right, e_left, e_right, path_len):
    if (s_left + e_right + 2) < path_len:
        return path_len - (s_left + e_right + 2)
    if (s_right + e_left + 2) < path_len:
        return path_len - (s_right + e_left + 2)
    return 0


def dfs(map, current_pos, end, visited, can_cheat):
    if current_pos == end:
        yield visited[current_pos]

    for dir in dirs:
        new_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
        if (new_pos in map and
            (new_pos not in visited or 
            visited[new_pos] > visited[current_pos]+1)):
            visited[new_pos] = visited[current_pos]+1 
            yield from dfs(map, new_pos, visited, can_cheat)

def get_path(visited, end, start):
    q = [end]
    path = {end: visited[end]}
    while len(q) > 0:
        current_pos = q.pop(0)
        #print(current_pos)
        #print_map(map_size+1, bytes, visited)

        if current_pos == start:
            return path
            
        for dir in dirs:
            new_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
            if (new_pos in visited and
                visited[current_pos] - visited[new_pos] == 1):
                q.append(new_pos)
                path[new_pos] = visited[new_pos]     

def bfs(map, start, end):
    q = [start]
    visited = {start:0}
    while len(q) > 0:
        current_pos = q.pop(0)
        #print(current_pos)
        #print_map(map_size+1, bytes, visited)

        if current_pos == end:
            return visited
            
        for dir in dirs:
            new_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
            if (new_pos in map and
               (new_pos not in visited or 
                visited[new_pos] > visited[current_pos]+1)):
                q.append(new_pos)
                visited[new_pos] = visited[current_pos]+1 

def print_path(map, path, width, height):
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in path:
                line += str(path[(x,y)]%10)
            elif (x,y) in map:
                line += '.'
            else: 
                line += '#'
        print(line)

def solve_part_2(file_name, cheat_len, cheat_th):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        map = []
        start = (0,0)
        end = (0,0)
        width = 0
        height = 0
        for y, line in enumerate(file.read().splitlines()):
            for x, letter in enumerate(line.strip()):
                if letter != '#':
                    map.append((x,y))
                if letter == 'S':
                    start = (x,y)
                if letter == 'E':
                    end = (x,y)
        width = x
        height = y

        len_from_start = bfs(map, start, end)
        basic_len = len_from_start[end]
        len_from_end = bfs(map, end, start)
        cuts = {}
        for start in len_from_start.items():
            for x in range(start[0][0]-cheat_len, start[0][0]+cheat_len+1):
                for y in range(start[0][1]-cheat_len, start[0][1]+cheat_len+1):
                    if (x,y) in len_from_end and abs(start[0][0]-x) + abs(start[0][1]-y) <= cheat_len and basic_len - (start[1] + len_from_end[(x,y)] + abs(start[0][0]-x) + abs(start[0][1]-y)) >= cheat_th:
                        if (basic_len - (start[1] + len_from_end[(x,y)] + abs(start[0][0]-x) + abs(start[0][1]-y))) in cuts:
                            cuts[basic_len - (start[1] + len_from_end[(x,y)] + abs(start[0][0]-x) + abs(start[0][1]-y))] += 1
                            #print(start[0], (x,y))
                        else:
                            cuts[basic_len - (start[1] + len_from_end[(x,y)] + abs(start[0][0]-x) + abs(start[0][1]-y))] = 1
                            #print(start[0], (x,y))

        for cut in cuts.items():
            print(f'{cut[1]} save {cut[0]}')
        #print(cuts)
        print(sum(cuts.values()))
def main():
    #solve_part_1('test.txt',2, 1)
    #solve_part_1('data.txt',2, 100)
    #solve_part_2('test.txt',2, 1)
    #solve_part_2('data.txt',2, 100)
    
    solve_part_2('test.txt',20, 50)
    solve_part_2('data.txt',20, 100)


if __name__ == "__main__":
    main()