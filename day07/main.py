import time

def solve(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name}')
        result, result2  = 0, 0

        for line in file.readlines():
            target, inputs = line.split(':')
            target = int(target)
            inputs = [int(i) for i in inputs.split()]

            result += target if dfs(target, inputs[0], inputs[1:], False) else 0
            result2 += target if dfs(target, inputs[0], inputs[1:], True) else 0
            
        print(f'Part 1 {result} \nPart 2 {result2}')

def dfs(result, current_result, inputs, part2):
    if inputs == []:
        return current_result == result
    else:
        if part2:
            if dfs(result, current_result + inputs[0], inputs[1:], part2):
                return 1
            if dfs(result, current_result * inputs[0], inputs[1:], part2):
                return 1
            if dfs(result, int(str(current_result)+str(inputs[0])), inputs[1:], part2):    
                return 1
            return 0
        else:
            if dfs(result, current_result + inputs[0], inputs[1:], part2):
                return 1
            if dfs(result, current_result * inputs[0], inputs[1:], part2):
                return 1
            return 0
        
def main():
    start = time.time()
    solve('test.txt')
    solve('data.txt')
    end = time.time()
    print(f'Time elapced {end - start}')

if __name__ == "__main__":
    main()