from collections import defaultdict

def solve_part_1(file_name, depth):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        result = 0
        all_buyers = []
        for line in file.read().splitlines():
            #print(line)
            secret = int(line.strip())
            
            prices = [secret%10]
            changes = []
            table = {}
            for i in range(depth):
                secret = (secret ^ (secret*64)) % 16777216
                secret = (secret ^ (secret//32)) % 16777216
                secret = (secret ^ (secret*2048)) % 16777216
                prices.append(secret%10)
                changes.append(prices[-1]-prices[-2])
                if len(changes) >= 4 and tuple(changes[-4:]) not in table:
                    table[tuple(changes[-4:])] = prices[-1]
            #for item in table.items():
            #    print(item)
            #    print(secret)
            #print('-----')
            all_buyers.append(table.copy())
            result += secret
        print('part1')
        print(result)
        combined_table = defaultdict(int)
        for buyer in all_buyers:
            for seq in buyer.items():
                combined_table[seq[0]] += seq[1]
        max_value = 0
        for seq in combined_table.items():
            if seq[1] >= max_value:
                print(seq)
                max_value = seq[1]
        print(max_value)


def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')


def main():
    #solve_part_1('test.txt', 2000)
    #solve_part_1('data.txt', 2000)
    #solve_part_1('test1.txt', 2000)
    solve_part_1('test2.txt', 2000)
    solve_part_1('data.txt', 2000)
    #solve_part_2('test.txt')
    #solve_part_2('data.txt')


if __name__ == "__main__":
    main()