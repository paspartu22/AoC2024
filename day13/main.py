import re

def solve(file_name):
    with open(file_name, 'r') as file:
        result = 0
        result2 = 0
        for game in file.read().split('\n\n'):
            result  += solve_part_1(game)
            result2 += solve_part_2(game)
            #print (f'{p1}, {p2}')
        print (result)
        print (result2)
def solve_part_1(game):
    lines = game.splitlines()
    
    A = [int(i) for i in re.findall("\\d+", lines[0])]
    B = [int(i) for i in re.findall("\\d+", lines[1])]
    target = [int(i) for i in re.findall("\\d+", lines[2])]
    
    results = []
    for i in range((target[0] // A[0])+1):
        b = (target[0] - A[0]*i)//B[0]
        if (A[0]*i + B[0]*b == target[0] and A[1]*i + B[1]*b == target[1]):
            results.append((i,b))
    
    #print(results)
    if len(results) > 0:
        #print(f'{A} {B} {target}')
        return (min([i[0]*3 + i[1] for i in results]))
    return 0

def solve_part_2(game):
    lines = game.splitlines()
    
    A = [int(i) for i in re.findall("\\d+", lines[0])]
    B = [int(i) for i in re.findall("\\d+", lines[1])]
    target = [int(i)+10000000000000 for i in re.findall("\\d+", lines[2])]
    #target = [int(i) for i in re.findall("\\d+", lines[2])]
    kA = A[1]/A[0]
    bA = 0
    kB = B[1]/B[0]
    bB = target[1] - kB*target[0]


    x = (bB-bA)/(kA-kB)
    xA = round(x/A[0])
    xB = round((target[0] - x) / B[0])
    # print(f'{A} {B} {target}')
    # print(f'yA = {kA}*x+{bA}  yB = {kB}*x+{bB}')
    # print (xA)
    # print (xB)
    # print(f'{target[0]} {int(xA*A[0] + xB*B[0])} {target[1]} {int(xA*A[1] + xB*B[1])}') 


    if (xA*A[0] + xB*B[0] == target[0] and target[1] == xA*A[1] + xB*B[1]):
        
        #print(f'{A} {B} {target}')
        return (int(xA*3 + xB))
    else:
        return 0
    #return (xA, xB)    
    #if (x*A[0] + x2*B[0] ==  target[0] and x*A[1] + x2*B[1] == target[1]):
    #    print(x)

        #   result += int(x*3 + B[0]//(target[0]-x))
    
    # print(results)
    # if len(results) > 0:
    #print(int(result))


def main():
    solve('test.txt')
    solve('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()