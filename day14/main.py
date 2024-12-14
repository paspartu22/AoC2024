import re

def solve_part_1(file_name, width, height, moves):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        results = [0,0,0,0]
        targets = []
        for line in file.read().splitlines():
            
            values =  re.findall('-?\d+', line)
            
            px, py, vx, vy = values
            tx = (int(px)+(int(vx)*moves))%(width)
            ty = (int(py)+(int(vy)*moves))%(height)
            targets.append((tx, ty))
            if (ty < height//2):
                if (tx < width//2):
                    results[0] += 1
                elif (tx > width//2):
                    results[1] += 1
            elif (ty > height//2):
                if (tx < width//2):
                    results[2] += 1
                elif (tx > width//2):
                    results[3] += 1
    
        draw_map (width, height, targets)
        print(results)
        print(results[0]*results[1]*results[2]*results[3])

def draw_map(widht, height, targets, output):
    #output.write('.012345678901\n')
    for y in range(height):
        line = str(y%10)
        for x in range(widht):
            value = 0
            for target in targets:
                if target == (x, y):
                    value += 1
            if value > 0:
                line += str(value)
            else:
                line += '.'
        output.write(f'{line}\n')
        #print(line)

def solve_part_2(file_name, width, height, space):
    robots = []
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        for line in file.read().splitlines():
            robot =  [int(i) for i in re.findall('-?\d+', line)]
            robots.append(robot)
    with open ('output.txt', 'a+') as output:
        results_list = []
        for move in range(10000):
            print(move)
            results = [0,0,0,0]
            for robot in robots:
                robot[0] = (robot[0] + robot[2]) % width
                robot[1] = (robot[1] + robot[3]) % height
                
                if (robot[1] < height//2 - space):
                    if (robot[0] < width//2 - space):
                        results[0] += 1
                    elif (robot[0] > width//2 + space):
                        results[1] += 1
                elif (robot[1] > height//2 + space):
                    if (robot[0] < width//2 - space):
                        results[2] += 1
                    elif (robot[0] > width//2 + space):
                        results[3] += 1
            
            if len(results_list) == 0 or measure_map(robots) > 300:
                output.write(f'{move}\n')
                print(move)
                draw_map(width, height, [(i[0], i[1]) for i in robots], output)

            results_list.append(measure_map(robots))
        output.write(f'{results_list}')
        print(results_list)

def measure_map(robots):
    sx = 0
    sy = 0
    for robot in robots:
        sx += robot[0]
        sy += robot[1]
    sx = sx // len(robots)
    sy = sy // len(robots)
    result = 0
    for robot in robots:
        result += 1/(abs(0.1*(robot[0]-sx))**20 + abs(0.1*(robot[1]-sy))**20 + 0.1)
    return result

def main():
    #solve_part_1('test.txt', 11, 7, 100)
    #solve_part_1('data.txt', 101, 103, 100)
    #solve_part_2('test.txt')
    solve_part_2('data.txt', 101, 103, 5)


if __name__ == "__main__":
    main()