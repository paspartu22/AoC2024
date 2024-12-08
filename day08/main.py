

def solve_part_1(file_name):
    nodes = {}
    map = {}
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        width = 0
        height = 0
        for y,line in enumerate(file.readlines()):
            width = len(line.strip())
            height += 1
            for x,letter in enumerate(line.strip()):
                map[(x, y)] = letter
                if letter != '.':
                    if letter not in nodes:
                        nodes[letter] = [(x, y)]
                    else:
                        nodes[letter].append((x,y))
        print(nodes)
        antinodes = []
        antinodes2 = []
        for node in nodes.items():
            for a in range(len(node[1])-1):
                for b in range(a+1, len(node[1])):
                    for antinode in get_antinodes(node[1][a], node[1][b]):
                        if antinode in map:
                            antinodes.append(antinode)
                            #map[antinode] = 'x'
                    for antinode in get_antinodes_part_2(node[1][a], node[1][b], map):
                        antinodes2.append(antinode) 
                        map[antinode] = 'x'
        print(len(set(antinodes)))
        print(len(set(antinodes2)))
        for i in range(12):
            line = ''
            for j in range(12):
                line += map[(j, i)]
            print(line)

def get_antinodes(antenna_1, antenna_2):
    antinode_1 = (antenna_1[0] + (antenna_1[0]-antenna_2[0]), antenna_1[1] + (antenna_1[1]-antenna_2[1]))
    antinode_2 = (antenna_2[0] + (antenna_2[0]-antenna_1[0]), antenna_2[1] + (antenna_2[1]-antenna_1[1]))
    return (antinode_1, antinode_2)     

def get_antinodes_part_2(antenna_1, antenna_2, map):
    antinodes = []
    i = 0
    while(1):
        antinode_1 = (antenna_1[0] + (antenna_1[0]-antenna_2[0])*i, antenna_1[1] + (antenna_1[1]-antenna_2[1])*i)
        antinode_2 = (antenna_2[0] + (antenna_2[0]-antenna_1[0])*i, antenna_2[1] + (antenna_2[1]-antenna_1[1])*i)
        i += 1
        if antinode_1 in map:
            antinodes.append(antinode_1)
        if antinode_2 in map:
            antinodes.append(antinode_2)
        if (antinode_1 not in map and antinode_2 not in map):
            return antinodes     




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