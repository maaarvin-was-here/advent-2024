

def process(f):
    a1, a2 = [], []
    with open(f, "r") as file:
        for line in file:
            a1.append(int(line.split(" ")[0]))
            a2.append(int(line.split(" ")[-1]))

    return (a1, a2)


def d1_1(a):
    a1 = a[0]
    a2 = a[1]

    a1.sort()
    a2.sort()

    sol = 0
    for i in range(0, len(a1)):
        sol += abs(a1[i] - a2[i])
    
    return(sol)


def d1_2(a):
    a1 = a[0]
    a2 = a[1]

    counts = {}

    for num in a2:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    
    sol = 0
    for num in a1:
        if num in counts:
            sol += int(num) * int(counts[num])
    
    return(sol)




if __name__ == '__main__':
    input_file = 'd1/d1.txt'
    list_object = process(input_file)
    sol_1 = d1_1(list_object)
    
    sol_2 = d1_2(list_object)

    print(sol_1)
    print(sol_2)