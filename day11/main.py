def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        stones = [int(i) for i in file.read().split()]
        print(stones)
        result = 0
        for move in range(6):
            #print(move)
            for i in range(len(stones)):
                if stones[i] == 0:
                    stones[i] = 1
                elif len(str(stones[i])) % 2 == 0:
                    stones.append(int(str(stones[i])[len(str(stones[i]))//2:]))
                    stones[i] = int(str(stones[i])[:len(str(stones[i]))//2])
                else:
                    stones[i] = stones[i]*2024
            print(f'{move} {len(stones)} {stones}')
        print(result + len(stones))

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        print(f'{file_name} part 1')
        stones = {}
        cash = {0:[1]}
        for stone in file.read().split():
            if stone in stones:
                stones[int(stone)] += 1
            else:
                stones[int(stone)] = 1
        
        for move in range(75):
            print(move)
            new_stones = {}
            for stone in stones.items():
                if stone[1] > 0:
                    if stone[0] in cash:
                        for new_stone in cash[stone[0]]:
                            if new_stone in new_stones:
                                new_stones[new_stone] += stone[1]
                            else:
                                new_stones[new_stone] = stone[1]

                    else:
                        if len(str(stone[0])) % 2 == 0:
                            value1 = int(str(stone[0])[:len(str(stone[0]))//2])
                            value2 = int(str(stone[0])[len(str(stone[0]))//2:])
                            if value1 in new_stones:
                                new_stones[value1] += stone[1]
                            else:
                                new_stones[value1] = stone[1]
                            if value2 in new_stones:
                                new_stones[value2] += stone[1]
                            else:
                                new_stones[value2] = stone[1]
                            cash[stone[0]] = [value1, value2]
                        else:
                            if stone[0]*2024 in new_stones:
                                new_stones[stone[0]*2024] += stone[1]
                            else:
                                new_stones[stone[0]*2024] = stone[1]

            stones = new_stones  
                             
        
        print(sum(stones.values()))
        #for move in range(25):

        #print(stones)

def main():
    #solve_part_1('test.txt')
    #solve_part_1('test3.txt')
    #solve_part_1('data.txt')
    solve_part_2('test2.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()