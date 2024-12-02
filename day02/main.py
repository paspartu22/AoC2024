UP = 0
DOWN = 1
valid = [[1, 2, 3], [-1, -2, -3]]

def solve(file_name):
    with open(file_name, 'r') as file:
        part_1_result = 0
        part_2_result = 0
        for line in file.readlines():
            report = [int(item) for item in line.split()]        
            part_1_result += check_report(report, 0, False, (report[1] - report[0] < 0))
            part_2_result += check_report(report, 0, True,  (report[1] - report[0] < 0))

        print(part_1_result)
        print(part_2_result)

def check_report(report, i,  can_dump, dir):
    if i == len(report)-1:
        return 1 #in the end
    else:
        if report[i+1] - report[i] in valid[dir]:
            return check_report(report, i+1, can_dump, dir) #Next step
                 
        elif can_dump: #dumping cases

            if (i <= 1 and check_report(report[1:], 0, False, (report[2]-report[1] < 0))):
                print(report)
                return 1
            
            if check_report(report[:i]+report[i+1:], i-1, False, dir if i > 1 else (report[i+1] - report[i-1] < 0)):
                print(report)
                return 1
            
            if check_report(report[:i+1]+report[i+2:], i, False, dir):
                print(report)
                return 1
            
        return 0
    
        


def main():
    solve('test.txt')
    solve('data.txt')


if __name__ == "__main__":
    main()
