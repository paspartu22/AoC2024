
def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        inputs, outputs = file.read().split('\n\n')
        inputs = inputs.split(', ')
        outputs = outputs.splitlines()
        
        result = 0
        for output in outputs:
            print(output)
            result +=  1 if 1 in check_output(inputs, output) else 0
        print(result)
#        print (inputs)
#        print (outputs)


def check_output(inputs, output):
   # print(output)
    for input in inputs:
        if output[:len(input)] == input:
            if len(output) == len(input):
                #print("Можно")
                yield 1
            else:
                yield from check_output(inputs, output[len(input):])
    #print("Нельзя")
    yield 0        


def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        inputs, outputs = file.read().split('\n\n')
        inputs = inputs.split(', ')
        outputs = outputs.splitlines()
        
            
        result = 0
        for output in outputs:
            results = [1]
            for i in range(1,len(output)+1): 
                results.append(0)
                for input in inputs:
                    if i >= len(input) and input == output[i-len(input):i]:
                        results[-1] += results[i-len(input)]
                #print(results)
            #print(results[-1])
            result += results[-1]
        print(result)

def main():
    #solve_part_1('test.txt')
    #solve_part_1('data.txt')
    solve_part_2('test.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()