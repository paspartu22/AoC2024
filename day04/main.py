dirs = [[-1,-1], [-1, 0], [-1, 1], 
        [0 ,-1],          [0 , 1],
        [1 ,-1], [1 , 0], [1 , 1]]
STRING = "XMAS"

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        lines={}
        width = 0
        height = 0
        for y,line in enumerate(file.readlines()):
            height += 1
            width = len(line)
            for x,letter in enumerate(line):
                lines[y,x] = letter
            #print(line.strip())
        result = 0
        for y in range(height):
            for x  in range(width):
                if lines[y,x] == 'X':
                    for dir in dirs:
                        for i,search in enumerate(STRING[1:]):
                            if ((y+(dir[0]*(i+1)),x+(dir[1]*(i+1))) in lines and 
                                lines[y+(dir[0]*(i+1)),x+(dir[1]*(i+1))] == search):
                                if lines[y+(dir[0]*(i+1)),x+(dir[1]*(i+1))] == STRING[-1]:
                                    result += 1
                            else:
                                break
        print(result)



def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        lines={}
        width = 0
        height = 0
        for y,line in enumerate(file.readlines()):
            height += 1
            width = len(line)
            for x,letter in enumerate(line):
                lines[y,x] = letter
            #print(line.strip())
        result = 0
        for y in range(height):
            for x  in range(width):
                if lines[y,x] == 'A':
                    if check_mas(lines, y, x):
                        result += 1

        print(result)
        
MAS = [{(-1, 1):'M', (1, -1) : 'S'},
       {(1, -1):'M', (-1, 1) : 'S'},
       {(1, 1) :'M', (-1, -1): 'S'},
       {(-1,-1):'M', (1, 1)  : 'S'}]

def check_mas(lines, y, x):
    result = 0
    for mas in MAS:
        for letter in mas.items():
            if (y+letter[0][0], x+letter[0][1]) in lines:
                new_char = lines[y+letter[0][0], x+letter[0][1]]
                if new_char != letter [1]:
                    break
                elif new_char == 'S':
                    result += 1
            else:
                break
    return result == 2


def main():
    solve_part_1('test.txt')
    solve_part_1('data.txt')
    solve_part_2('test.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()