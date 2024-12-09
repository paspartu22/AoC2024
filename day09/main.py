class Segment:
    def __init__(self, start, len, id) -> None:
        self.start = int(start)
        self.len = int(len)
        self.id = int(id)
        self.moved = False

    def __str__(self) -> str:
        return f'start {self.start}, len {self.len}, id {self.id}' 
    
    def checksum(self):
        result = 0
        for i in range(self.start, self.start+self.len):
            result += self.id*i
        return result

def solve_part_1(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 1')
        space = []
        line = file.read().strip()
        for i in range(len(line)//2):
            for j in range(int(line[i*2])):
                space.append(i)
            for j in range(int(line[i*2+1])):
                space.append(-1)
        for j in range(int(line[-1])):
            space.append((len(line)//2))
        #print(space)
        while (-1 in space):
            last = space.pop()
            if (last != -1):    
                space[space.index(-1)] = last
                #print(space)
        #print(space)
        result = 0
        for i, item in enumerate(space):
            result += i*item
        print(result)

def solve_part_2(file_name):
    with open(file_name, 'r') as file:
        print(f'{file_name} part 2')
        line = file.read().strip()
        segments = []

        mem_pointer = 0
        for i in range(len(line)//2):
            segments.append(Segment(mem_pointer, line[i*2], i))
            mem_pointer += int(line[i*2])
            segments.append(Segment(mem_pointer, line[i*2 +1], -1))
            mem_pointer += int(line[i*2 +1])
        segments.append(Segment(mem_pointer, line[-1], len(line)//2))
        i = len(segments)-1
        for segment in segments:
            print(segment)
        print('---')
        while i > 0:
            #print(segments[i])
            #if segments[-1].id == -1:
            #    segments.pop()
            #    i -= 1
            if segments[i].id != -1:
                for j in range(i):
                    if segments[j].id == -1 and segments[j].len >= segments[i].len and segments[i].moved == False :
                        segments[i].moved = True
                        segments[i].start = segments[j].start
                        #if segments[j].len == segments[i].len:
                        #    segments.pop(i)
                        #else:
                        segments[j].start += segments[i].len
                        segments[j].len -= segments[i].len
                        #i += 1
                        break
            i -= 1
        result = 0
        for segment in segments:
            if segment.len != 0:
                print(segment)
            if segment.id > -1:
                result += segment.checksum()
        print(result)

def main():
    #solve_part_1('test.txt')
    #solve_part_1('data.txt')
    solve_part_2('test.txt')
    solve_part_2('data.txt')


if __name__ == "__main__":
    main()