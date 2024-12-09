import os

DEBUG = False

def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            temp = []
            for i in range(0, len(line)):
                if line[i] != '\n':
                    val = int(line[i])
                    if i%2 == 0:    # represents file object
                        cur_id = i//2
                        for j in range(0, val):
                            temp.append(cur_id)
                    else:           # represents free space
                        for j in range(0, val):
                            temp.append('.')
            arr.append(temp)
    return arr


def dbpr(x):
    if DEBUG:
        print(x)
    

def d9_1(input):
    l, r = 0, len(input)-1

    while l < r:
        if input[l] != '.':
            l += 1
            dbpr("moving left forward to " + str(l))
        elif input[r] == '.':
            r -= 1
            dbpr("moving right back to " + str(r))
        else:
            dbpr("switching at " + str((l,r)))
            input[l] = input[r]
            input[r] = '.'
            r-=1
    
    sol = 0
    for i in range(0, len(input)):
        if input[i] != '.':
            sol += i * input[i]
    return sol


def process_2(f):
    arr = []
    with open(f, "r") as file:
        free_dict = {}
        file_dict = {}
        for line in file:
            temp = []
            for i in range(0, len(line)):
                if line[i] != '\n':
                    val = int(line[i])
                    if i%2 == 0:    # represents file object
                        file_id = i//2
                        file_dict[file_id] = (val, len(temp))
                        for j in range(0, val):
                            temp.append(file_id)
                    else:           # represents free space
                        if val != 0:
                            free_dict[i] = (val, len(temp)) # number of spaces, index of start
                            for j in range(0, val):
                                temp.append('.')
                        
            arr.append(temp)
            dbpr("free")
            dbpr(free_dict)
            dbpr("file")
            dbpr(file_dict)
    return arr[0], free_dict, file_dict


def d9_2(input, free_dict, file_dict):
    s_file_k = sorted(file_dict.keys(), reverse=True)
    s_free_k = sorted(free_dict.keys())
    
    dbpr(s_free_k)

    counter = 0
    total = len(s_file_k)
    for file_key in s_file_k:
        counter += 1
        dbpr(int(100 * counter/total))
        file_size, file_index = file_dict[file_key]
        for free_key in s_free_k:
            free_size, free_index = free_dict[free_key]
            if free_size >= file_size and free_index < file_index:
                dbpr(str(file_key) + " starts at " + str(file_index))
                dbpr(str(file_key) + " fits at " + str(free_index))

                dbpr("before " + str(input))
            

                for i in range(free_index, free_index + file_size):
                    input[i] = file_key
                for i in range(file_index, file_index + file_size):
                    input[i] = '.'

                dbpr("after " + str(input))

                free_dict[free_key] = (free_size - file_size, free_index + file_size)

                dbpr("new free dict " + str(free_dict))

                # print(input)

                break

    
    # print(input)
    sol = 0
    for i in range(0, len(input)):
        if input[i] != '.':
            sol += i * input[i]
    return sol


if __name__ == '__main__':
    input_file = '{}/d9.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)[0]
    if(DEBUG):
        print(list)

    list2, free_dict, file_dict = process_2(input_file)

    sol_1 = d9_1(list)
    sol_2 = d9_2(list2, free_dict, file_dict)

    print(sol_1)
    print(sol_2)


# 8551696246309 is too high