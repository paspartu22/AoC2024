UP = 0
DOWN = 1
valid = [[1, 2, 3], [-1, -2, -3]]

def solve(file_name):
    with open(file_name, 'r') as file:
        part_1_result = 0
        part_2_result = 0
        for line in file.readlines():
            report = [int(item) for item in line.split()]
            print(report)           
            part_1_result += check_report(report, False, (report[1] - report[0] < 0), True)
            part_2_result += check_report(report, True,  (report[1] - report[0] < 0), True)
#            if check_report(report, True,  (report[1] - report[0] < 0), True):
#                print(report)
        print(part_1_result)
        print(part_2_result)

def check_report(report, can_dump, dir, start):
    if len(report) == 2:
        return True
    else:
        if report[2 - start] - report[1 - start] in valid[dir]:
            return check_report(report[1 - start:], can_dump, dir, False)
        
        elif can_dump:
            if (start and check_report(report[1:], False, (report[2]-report[1] < 0), False)):
                return 1
            
            if len(report) == 3:
                return 1
            
            
            new_report = report.copy()
            new_report.pop(1)
            if check_report(new_report, False, dir, True):
                return 1
            
            new_report = report.copy()
            new_report.pop(2)
            if check_report(new_report, False, dir, False):
                return 1
            
            return 0
        else:
            return 0
    
        


def main():
    solve('test.txt')
    solve('data.txt')


if __name__ == "__main__":
    main()

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        result = 0
        for line in file.readlines():
            report = [int(item) for item in line.split()]
            result += check_report(report, False)
        print(result)

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        result = 0
        for line in file.readlines():
            report = [int(item) for item in line.split()]
            #print(report)
            if check_report(report) :
                result += 1
            else:
                #print('removing')
                for i in range(len(report)):
                    new_array = report.copy()
                    new_array.pop(i)
                    #print(new_array)
                    if check_report(new_array):
                        result += 1
                        break
                #print('end removing')

        print(result)
