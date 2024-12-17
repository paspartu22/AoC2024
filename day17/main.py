def calc_opp(pointer, registers, opp_code, arg, output = [], forced_end = False):
    if opp_code == 0: 
        # The adv instruction (opcode 0) performs division. 
        # The numerator is the value in the A register. 
        # The denominator is found by raising 2 to the power of the instruction's combo. 
        # The result of the division operation is truncated to an integer and then written to the A register.operand.
        if arg < 4:
            registers[0] = registers[0]//(2**arg)
        else:
            registers[0] = registers[0]//(2**registers[arg-4])
        return pointer + 2
    elif opp_code == 1:
        # calculates the bitwise XOR of register B and the instruction's literal operand, 
        # then stores the result in register B.
        registers[1] = registers[1]^arg
        return pointer + 2
    elif opp_code == 2:
        # calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), 
        # then writes that value to the B register.
        if arg < 4:
            registers[1] = arg % 8
        else:
            registers[1] = registers[arg-4] % 8
        return pointer + 2
    elif opp_code == 3:
        # does nothing if the A register is 0. 
        # However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; 
        # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        if registers[0] == 0 or forced_end:
            return pointer + 2
        else:
            return arg
    elif opp_code == 4:
        # calculates the bitwise XOR of register B and register C, then stores the result in register B. 
        # (For legacy reasons, this instruction reads an operand but ignores it.)
        registers[1] = registers[1]^registers[2]
        return pointer + 2
    elif opp_code == 5:
        # calculates the value of its combo operand modulo 8, then outputs that value. 
        # (If a program outputs multiple values, they are separated by commas.)
        if arg < 4:
            output.append(arg)
            #print(f'{arg},', end= '')
        else:
            output.append(registers[arg-4]%8)
            #print(f'{registers[arg-4]%8},', end= '')
        return pointer + 2
    elif opp_code == 6:
        # works exactly like the adv instruction except that the result is stored in the B register. 
        # (The numerator is still read from the A register.)
        if arg < 4:
            registers[1] = registers[0]//(2**arg)
        else:
            registers[1] = registers[0]//(2**registers[arg-4])
        return pointer + 2
    elif opp_code == 7:
        # works exactly like the adv instruction except that the result is stored in the C register. 
        # (The numerator is still read from the A register.)
        if arg < 4:
            registers[2] = registers[0]//(2**arg)
        else:
            registers[2] = registers[0]//(2**registers[arg-4])
        return pointer + 2    

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        reg, programm = file.read().split('\n\n')
        reg = [int(re.split(':')[1]) for re in reg.splitlines()]
        programm = [int(p) for p in programm.split(':')[1].split(',')]
        pointer = 0
        print(programm)
        
        output = []
        while pointer < len(programm):
            pointer = calc_opp(pointer, reg, programm[pointer], programm[pointer+1], output)
        #print('end')
        result = ''
        for i in output:
            result += f'{i},'
        print(result[:-1])
        
def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        reg, programm = file.read().split('\n\n')
        reg = [int(re.split(':')[1]) for re in reg.splitlines()]
        programm = [int(p) for p in programm.split(':')[1].split(',')]
        print(programm)
        result = list(dfs(programm, -1, 0))
        print(min(result))

def dfs(programm, num, end):
    for a in range(end*8, (end+1)*8):
        reg = [a, 0, 0]
        pointer = 0    
        output = []
        while pointer < len(programm):
            pointer = calc_opp(pointer, reg, programm[pointer], programm[pointer+1], output, True)
        if reg[1]%8 == programm[num]:
            if -num == len(programm):
                yield(a)
            else:
                yield from dfs(programm, num-1, a)
      

def test_cases():
    print('---')
    pointer = 0
    reg = [117440,0,0]
    programm = [0,3,5,4,3,0]
    output = []
    while pointer < len(programm):
        pointer = calc_opp(pointer, reg,  programm[pointer], programm[pointer+1], output)
    print()
    print(reg)
    print(output)
    print(output == programm)
    print('---')

    pointer = 0
    programm = [2, 6]
    reg = [0,0,9]
    calc_opp(pointer, reg, programm[pointer], programm[pointer+1])
    print()
    print(reg)

    print('---')
    pointer = 0
    reg = [10,0,0]
    programm = [5, 0, 5, 1, 5, 4]
    output = []
    while pointer < len(programm):
        pointer = calc_opp(pointer, reg,  programm[pointer], programm[pointer+1], output)
    print()
    print(reg)
    print(output)
    print('---')

    pointer = 0
    reg = [2024,0,0]
    programm = [0,1,5,4,3,0]
    while pointer < len(programm):
        pointer = calc_opp(pointer, reg,  programm[pointer], programm[pointer+1])
    print()
    print(reg)

    print('---')

def main():
    #test_cases()
    #solve_part_1('test.txt')
    solve_part_1('data.txt')
    #solve_part_2('test2.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()