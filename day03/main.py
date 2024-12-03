import re


def solve_part_1_re(file_name):
    print(f'{file_name} part 1')
    print(sum(
          int(re.split('\(|,|\)', item)[1]) 
         *int(re.split('\(|,|\)', item)[2]) 
          for item in 
          re.findall('mul\(\d{,3},\d{,3}\)', open(file_name, 'r').readline())))

def solve_part_2_re(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')

        re_line = "don't\(\)|do\(\)|mul\(\d{,3},\d{,3}\)" 
        line = file.readline()
        result = 0
        do = 1
        for item in re.findall(re_line, line):
            #print(item)
            if (item == "do()"):
                do = 1
            elif (item == "don't()"):
                do = 0
            else:
                item = re.split('\(|,|\)', item)
                result += int(item[1])*int(item[2])*do

        print(result)


def main():
    solve_part_1_re('test.txt')
    solve_part_1_re('data.txt')
    solve_part_2_re('test2.txt')
    solve_part_2_re('data.txt')


if __name__ == "__main__":
    main()