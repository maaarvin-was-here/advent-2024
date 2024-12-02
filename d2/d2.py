

def process(f):
    lines = []
    with open(f, "r") as file:
        for line in file:
            spl = line.split(" ")
            nums = [int(s) for s in spl]
            lines.append(nums)
    return lines


def is_valid(report):
    l, r = 0, 1
    if report[l] > report[r]:   
        # descending
        while r < len(report):
            # print("checking " + str(report[l]) + " and " + str(report[r]))
            if report[l] <= report[r] or report[l] - report[r] > 3:
                return False
            l += 1
            r += 1
    else:   
        # ascending
        while r < len(report):
            # print("checking " + str(report[l]) + " and " + str(report[r]))
            if report[l] >= report[r] or report[r] - report[l] > 3:
                return False
            l += 1
            r += 1
    
    return True


def is_valid_2(report):
    # print(report)
    for i in range(0, len(report)):
        r = report.copy()
        r.pop(i)
        # print(r)
        if is_valid(r):
            return True
    return False



def d2_1(l):
    sol = 0
    for report in l:
        if(is_valid(report)):
            sol += 1
    return(sol)


def d2_2(l):
    sol = 0
    for report in l:
        if(is_valid_2(report)):
            sol += 1
    return sol  



if __name__ == '__main__':
    input_file = 'd2/d2.txt'
    list = process(input_file)

    print(d2_1(list))
    print(d2_2(list))
