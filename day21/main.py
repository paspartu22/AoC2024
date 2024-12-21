kpad = {
    '7':(0,0),
    '8':(1,0),
    '9':(2,0),
    '4':(0,1),
    '5':(1,1),
    '6':(2,1),
    '1':(0,2),
    '2':(1,2),
    '3':(2,2),
    '0':(1,3),
    'A':(2,3),
}

dpad = {
    '^':(1,0),
    'A':(2,0),
    '<':(0,1),
    'v':(1,1),
    '>':(2,1),
}

memo = {}

def get_path_pad(pad, cur, new):

    horisontal = ''
    vertical = ''
    if (pad[cur][0] > pad[new][0]):
        horisontal = '<'*(pad[cur][0] - pad[new][0])
    else:
        horisontal = '>'*(pad[new][0] - pad[cur][0])
    if (pad[cur][1] > pad[new][1]):
        vertical = '^'*(pad[cur][1] - pad[new][1])
    else:
        vertical = 'v'*(pad[new][1] - pad[cur][1])

    if horisontal == '' or vertical == '':
        return [horisontal+vertical+'A']
    
    output = [horisontal+vertical+'A', vertical+horisontal+'A']
    
    if pad == dpad: 
        if pad[new][0] == 0:
            output.pop(0)
        elif pad[cur][0] == 0:
            output.pop()
    elif pad == kpad: 
        if pad[new][0] == 0 and pad[cur][1] == 3:
            output.pop(0)
        elif pad[cur][0] == 0 and pad[new][1] == 3:
            output.pop()            
    return set(output)

def dfs_pad(pad, line, i, cur, new, output):              
    path = get_path_pad(pad, cur, new)
    for p in path:
        if i == len(line)-1:
            yield output+p
        else:
            yield from dfs_pad(pad, line, i+1, new, line[i+1], output+p)

def dfs_top(line, depth):
    if depth == 0:
        return len(line)
    else:
        lines = [i+'A' for i in line.split('A')[:-1]]
        lenght = 0
        for small_line in lines:
            if (small_line, depth) in memo:
                lenght += memo[(small_line, depth)]
            else:
                
                paths = list(dfs_pad(dpad, small_line, 0, 'A', small_line[0], ""))
                lenghts = []
                for p in paths:
                    lenghts.append(dfs_top(p, depth-1))
                lenght += min(lenghts)
                memo[(small_line, depth)] = (min(lenghts)) 
        return lenght
    
def solve_part_1(file_name, depth):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        result = 0
        for line in file.read().splitlines():
            print(line)
            outputs = list(dfs_pad(kpad, line.strip(), 0, 'A', line[0], ""))
            print(outputs)
            len = 0
            for output in outputs:
                if len == 0:
                    len = dfs_top(output, depth)
                else:
                    len = min(len, dfs_top(output, depth))
                    
            result += len * int(line[:-1])
            print(len)
        print(result)


def main():
    solve_part_1('test.txt', 2)
    solve_part_1('data.txt', 2)
    solve_part_1('test.txt', 25)
    solve_part_1('data.txt', 25)


if __name__ == "__main__":
    main()