        #UP     RIGHT   DOWN   LEFT         
dirs = [[0,-1], [1,0],  [0,1], [-1,0]]

def solve_part_1(file_name, bytes_len, map_size):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        bytes = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in file.read().splitlines()]
        bytes = bytes[:bytes_len]

        return (bfs(bytes, map_size)[0])
        #print(bytes)

def print_map(size, bytes, visited):
    print('#0123456')
    for y in range(size):
        line = str(y)
        for x in range(size):
            if (x, y) in bytes:
                line += "#"
            elif (x, y) in visited:
                line += str(visited[(x,y)]%10)
            else:
                line += "."
        print(line)

def bfs(bytes, map_size):
    q = [(0,0)]
    visited = {(0, 0):0}
    map_size -= 1
    while len(q) > 0:
        current_pos = q.pop(0)
        #print(current_pos)
        #print_map(map_size+1, bytes, visited)

        if current_pos == (map_size, map_size):
            return (visited[current_pos], visited)
            break
        for dir in dirs:
            new_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
            if (new_pos[0] >= 0 and new_pos[0] <= map_size and 
                new_pos[1] >= 0 and new_pos[1] <= map_size and
                new_pos not in bytes and
                (new_pos not in visited or visited[new_pos] > visited[current_pos]+1)):
                q.append(new_pos)
                visited[new_pos] = visited[current_pos]+1 
    return (0, 0)


def solve_part_2(file_name, bytes_len, map_size):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        bytes = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in file.read().splitlines()]

        path = bfs(bytes[:bytes_len], map_size)[1]
        bound = [bytes_len, len(bytes)]
        while 1:
            bytes_len = bound[0] + (bound[1]-bound[0])//2
            print(bytes_len)
            print(bound)
            new_byte = bytes[bytes_len-1]
            lenght,path = bfs(bytes[:bytes_len], map_size)
            if lenght == 0:
                bound[1] = bytes_len
            else:
                bound[0] = bytes_len
            if bound[1] - bound[0] <= 1:
                print(bound)
                return bytes[bound[0]]


def main():
    #print(solve_part_1('test.txt', 12, 7))
    #print(solve_part_1('data.txt', 1024, 71))
    print(solve_part_2('test.txt', 12, 7))
    print(solve_part_2('data.txt', 1024, 71))


if __name__ == "__main__":
    main()