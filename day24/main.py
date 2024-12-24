import operator
from pprint import pprint
op_dict = {
    'AND' : operator.and_,
    'OR'  : operator.or_,
    'XOR' : operator.xor
}

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        start, switches = file.read().split('\n\n')
        wires = {}       
        for line in start.splitlines():
            wire, value = line.split(':')
            wires[wire] = int(value)
        gates = {}
        named_gates = {}
        for gate in switches.splitlines():
            gate = gate.split(' ')
            gate_name = gate[-1]
            if ('x' in str(gate[0])+str(gate[2]) and 'y' in str(gate[0])+str(gate[2])):
                if gate[1] == 'XOR':
                    named_gates[gate_name] = f'z{gate[0][1:]}s'
                if gate[1] == 'AND':
                    named_gates[gate_name] = f'z{gate[0][1:]}c'
            gates[gate_name] = (gate[:3])
        
        #print(gates)
        swaps = [
            ['grf','wpq'],
            ['fvw','z18'],
            ['nwq','z36'], 
            ['mdb','z22']
        ]
        for swap in swaps:
            swap_gates(swap, gates, named_gates)

        part2 = {}
        #part2['z00'] = ['z00s']
        for i in range(1,47):    
            if f'z{i:02d}' in gates:
                part2[f'z{i:02d}'] = dfs(gates, f'z{i:02d}', 100, named_gates)
            else:
                break
        print('----')
        #pprint(part2)
        
        for item in part2.items():
            if item[0] == 'z18':
                pass
            check = collapse_bit(int(item[0][1:]), item[1])
            print(f'{item} {check}')
        line = ''
        for i in sorted(['grf','wpq','fvw','z18','nwq','z36','mdb','z22']):
            line += i+','
        print(line[:-1])
        
        #part1
        '''
        while gates:
            for gate in gates.items():
                if gate[1][0] in wires and gate[1][2] in wires:
                    wires[gate[0]] = op_dict[gate[1][1]](wires[gate[1][0]], wires[gate[1][2]])
                    del gates[gate[0]]
                    break
        i = 0
        result = 0
        while 1:
            #print(f'z{i:02d}')
            if f'z{i:02d}' in wires:
                result += wires[f'z{i:02d}'] * 2**i
                #print(wires[f'z{i:02d}'])
            else:
                break
            i += 1
        print(result)
      
        '''
def swap_gates(swap, dict, dict2):
    dict[swap[0]], dict[swap[1]] = dict[swap[1]], dict[swap[0]] 
    if swap[0] in dict2 and swap[1] in dict2:
        dict2[swap[0]], dict2[swap[1]] = dict2[swap[1]], dict2[swap[0]] 
    
def collapse_bit(bit, eval):
    _bit = bit if eval[1] == 'OR' else bit -1
    if not isinstance(eval[0], str):
        eval[0] = collapse_bit(_bit, eval[0])
    if not isinstance(eval[2], str):
        eval[2] = collapse_bit(_bit, eval[2])
        
    if 'XOR' in eval and f'z{bit:02d}s' in eval and f'z{bit-1:02d}c' in eval:
        return bit
    if 'AND' in eval and f'z{bit:02d}s' in eval and f'z{bit-1:02d}c' in eval:
        return f'z{bit:02d}c'
    if 'OR' in eval and f'z{bit:02d}c' in eval:
        return f'z{bit:02d}c'
    #elif 'AND' in eval and f'{bit}s'
    
    
    
def dfs(gates, id, depth, named_gates):
    if depth == 0:
        return gates[id]
    else:
        result = gates[id].copy()
        if result[0] in gates:
            if result[0] not in named_gates:
                result[0] = dfs(gates, result[0], depth-1, named_gates)
            else:
                result[0] = named_gates[result[0]]
        if result[2] in gates:
            if result[2] not in named_gates:
                result[2] = dfs(gates, result[2], depth-1, named_gates)
            else:
                result[2] = named_gates[result[2]]
        return result

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')


def main():
    #solve_part_1('test.txt')
    #solve_part_1('test2.txt')
    solve_part_1('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()