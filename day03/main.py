import re


def solve_part_1_re(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        print(sum(
             int(re.split('\(|,|\)', item)[1]) 
            *int(re.split('\(|,|\)', item)[2]) 
            for item in 
            re.findall('mul\(\d{,3},\d{,3}\)', file.readline())))



def solve_part_2_re(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        result = 0
        line = file.readline()

# 
        re_line = "don't\(\)|do\(\)|mul\(\d{,3},\d{,3}\)" 
        x = re.findall(re_line, line)
        result = 0
        do = 1
        for item in x:
            print(item)
            if (item == "do()"):
                do = 1
            elif (item == "don't()"):
                do = 0
            else:

                num1, num2 = item.split(',')
                num1 = num1[4:]
                num2 = num2[:-1]
                #print (num1)
                #print (num2)
                result += int(num1)*int(num2)*do
        #print(x)
        print(result)

def get_number(line, start, ender):
    for i in range(4):
        item = line[start+i]
        if i>0 and line[start+i] == ender:
            return line[start:start+i]
        elif not line[start+i].isdigit():
            return -1 
    return -1

def main():
    solve_part_1_re('test.txt')
    solve_part_1_re('data.txt')
    solve_part_2_re('test2.txt')
    solve_part_2_re('data.txt')


if __name__ == "__main__":
    main()