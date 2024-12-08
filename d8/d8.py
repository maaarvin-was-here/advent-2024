import os

DEBUG = False

def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            temp = []
            for char in line:
                if char != '\n':
                    temp.append(char)
            arr.append(temp)
    return arr


def d8_1(grid):
    rows, cols = len(grid), len(grid[0])

    antenna_list = {}
    # (row, col),  y, x
    for r in range(0, rows):
        for c in range(0, cols):
            if grid[r][c] != '.':
                cur_ant = grid[r][c]
                if cur_ant not in antenna_list:
                    antenna_list[cur_ant] = []
                antenna_list[cur_ant].append((r, c))

    
    antinodes = set()

    for key in antenna_list.keys():
        coords = antenna_list[key]
        
        # get every pair combo
        for i in range(0, len(coords)):
            for j in range(i + 1, len(coords)):
                c1 = coords[i]
                c2 = coords[j]
                # print(c1, c2)

                # find difference between x and y values of each point, then add that to the smallest 

                c1_r, c1_c = c1[0], c1[1]
                c2_r, c2_c = c2[0], c2[1]

                dr = abs(c1_r - c2_r)
                dc = abs(c1_c - c2_c)

                if c1_r > c2_r:
                    c1_r += dr
                    c2_r -= dr
                else:
                    c1_r -= dr
                    c2_r += dr
                
                if c1_c > c2_c:
                    c1_c += dc
                    c2_c -= dc
                else:
                    c1_c -= dc
                    c2_c += dc
                
                n1 = (c1_r, c1_c)
                n2 = (c2_r, c2_c)

                if c1_r in range(0, rows) and c1_c in range(0, cols):
                    antinodes.add((c1_r, c1_c))
                if c2_r in range(0, rows) and c2_c in range(0, cols):
                    antinodes.add((c2_r, c2_c))
    
    return len(antinodes)


def ceildiv(a, b):
    return -( a // -b)


def d8_2(grid):
    rows, cols = len(grid), len(grid[0])
    if(DEBUG):
        print(rows, cols)

    antenna_list = {}
    # (row, col),  y, x
    for r in range(0, rows):
        for c in range(0, cols):
            if grid[r][c] != '.':
                cur_ant = grid[r][c]
                if cur_ant not in antenna_list:
                    antenna_list[cur_ant] = []
                antenna_list[cur_ant].append((r, c))

    
    antinodes = set()

    for key in antenna_list.keys():
        coords = antenna_list[key]
        if(DEBUG):
            print(" ")
            print("looking at " + key)
        
        # get every pair combo
        for i in range(0, len(coords)):
            for j in range(i + 1, len(coords)):
                c1 = coords[i]
                c2 = coords[j]
                if(DEBUG):
                    print(c1, c2)

                c1_r, c1_c = c1[0], c1[1]
                c2_r, c2_c = c2[0], c2[1]

                dr = abs(c1_r - c2_r)
                dc = abs(c1_c - c2_c)

                if(DEBUG):
                    print("hop " + str((dr, dc)))
                    print(c1)
                
                if c1_r > c2_r:
                    if c1_c > c2_c:
                        # c1 both positive
                        if(DEBUG):
                            print("+ +")
                        r_to_edge = rows - c1_r
                        c_to_edge = cols - c1_c
                        r_sign, c_sign = 1, 1
                        pass
                    else:
                        # c1 positive rows, negative cols
                        if(DEBUG):
                            print("+ -")
                        r_to_edge = rows - c1_r
                        c_to_edge = c1_c
                        r_sign, c_sign = 1, -1
                        pass
                else:
                    if c1_c > c2_c:
                        # c1 negative rows, positive cols
                        if(DEBUG):
                            print("- +")
                        r_to_edge = c1_r
                        c_to_edge = cols - c1_c
                        r_sign, c_sign = -1, 1
                        pass
                    else:
                        # c1 both negative, c1_r, c1_c represents distance from 0,0
                        if(DEBUG):
                            print("- -")
                        r_to_edge = c1_r
                        c_to_edge = c1_c
                        r_sign, c_sign = -1, -1
                        pass
                
                num_hops = min(ceildiv(r_to_edge, dr), ceildiv(c_to_edge, dc))
                if(DEBUG):
                    print("hops: " + str(num_hops))
                
                start_point = (c1_r + (r_sign * num_hops * dr), c1_c + (c_sign * num_hops * dc))
                if(DEBUG):
                    print("start " + str(start_point))

                if not (start_point[0] in range(0, rows) and start_point[1] in range(0, cols)):
                    nsr = start_point[0] + (dr * -1 * r_sign)
                    nsc = start_point[1] + (dc * -1 * c_sign)
                
                    start_point = (nsr, nsc)

                cur = start_point
                while cur[0] in range(0, rows) and cur[1] in range(0, cols):
                    if(DEBUG):
                        print(cur)
                    tr = cur[0]
                    tc = cur[1]
                    if tr in range(0, rows) and tc in range(0, cols):
                        if(DEBUG):
                            print("appending")
                        antinodes.add((tr, tc))
                    ntr = tr + (dr * -1 * r_sign)
                    ntc = tc + (dc * -1 * c_sign)
                    cur = (ntr, ntc)

    
    return len(antinodes)



if __name__ == '__main__':
    input_file = '{}/d8.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)
    if(DEBUG):
        print(list)

    sol_1 = d8_1(list)
    sol_2 = d8_2(list)

    print(sol_1)
    print(sol_2)