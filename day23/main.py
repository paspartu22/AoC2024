import networkx as nx

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        edges = [line.split('-') for line in file.read().splitlines()]
        g = nx.from_edgelist(edges)
        cliques = nx.find_cliques(g)
        result =  sorted(max(cliques, key=len))

        line = ''
        for i in result:
            line += i +','            
        print(line[:-1])
        
def main():
    solve_part_1('test.txt')
    solve_part_1('data.txt')
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()

