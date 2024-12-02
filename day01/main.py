
with open('data.txt') as file:
    a = []
    b = []
    for line in file.readlines():
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))
    a.sort()
    b.sort()
    #sum = 0
    #sum2 = 0
    #for i in range(len(a)):
    #    sum += (abs(b[i] - a[i]))
    #    sum2 += (a[i]*b.count(a[i]))
        #print(f'{a[i]} {b[i]} {b.count(a[i])}')
        #print(sum2)
    #print("++")
    #print(sum)
    #print(f'{sum ([abs(b[i] - a[i] for i in range(len(a))) ] )} \n ')
    print(sum([a[i]*b.count(a[i]) for i in range(len(a))]))