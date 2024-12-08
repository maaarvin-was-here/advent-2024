import os
import copy

def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            arr_item = []
            for x in line:
                if x != '\n':
                    arr_item.append(x)
            arr.append(arr_item)
    return arr


def d6_1(grid):
    rows, cols = len(grid), len(grid[0])

    for i in range(0, rows):
        if '^' in grid[i]:
            start = (i, grid[i].index('^'))

    print(start)

    directions = [
        (-1,0), # up
        (0, 1), # right
        (1, 0), # down
        (0, -1) # left
    ]
    
    cur = start
    d = 0
    visited = []
    visited.append(cur)
    while 1:
        r = cur[0]
        c = cur[1]
        # print("at " + str(r) + " " + str(c))
        
        dr, dc = directions[d]
        new_r = r + dr
        new_c = c + dc

        if new_r in range(0, rows) and new_c in range(0, cols):
            if grid[new_r][new_c] != '.' and grid[new_r][new_c] != '^':
                if d != 3:
                    d += 1
                else:
                    d = 0
            else:
                cur = new_r, new_c
                if cur not in visited:
                    visited.append((new_r, new_c))
        else:
            sol = len(visited)
            visited.remove(start)
            return sol, visited


def is_cyclic(grid):
    rows, cols = len(grid), len(grid[0])

    for i in range(0, rows):
        if '^' in grid[i]:
            start = (i, grid[i].index('^'))

    directions = [
        (-1,0), # up
        (0, 1), # right
        (1, 0), # down
        (0, -1) # left
    ]
    
    cur = start
    d = 0
    visited = set()

    # counter = 0
    while 1:
        # counter += 1
        # print(counter)
        r = cur[0]
        c = cur[1]

        if (r, c, d) in visited:
            return True
        visited.add((r, c, d))
        
        dr, dc = directions[d]
        new_r = r + dr
        new_c = c + dc

        if new_r in range(0, rows) and new_c in range(0, cols):
            if (grid[new_r][new_c] != '.' and grid[new_r][new_c] != '^'):
                d = (d+1)%4
            else:
                cur = new_r, new_c
            
        else:
            break
    
    return False


def d6_2(grid, visited):
    sol = 0
    counter = 0
    total = len(visited)
    for r, c in visited:
        counter += 1
        print("Percent Done: " + str(int(100 * (counter/total))) + "%")
        temp = copy.deepcopy(grid)
        temp[r][c] = '#'
        if is_cyclic(temp):
            sol += 1
    return(sol)


if __name__ == '__main__':
    input_file = '{}/d6.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    p1_sol, visited = d6_1(list)
    p2_sol = d6_2(list, visited)
    
    print(p1_sol)
    print(p2_sol)


'''
used to debug



def d6_22(grid):
    rows, cols = len(grid), len(grid[0])

    for i in range(0, rows):
        if '^' in grid[i]:
            start = (i, grid[i].index('^'))
    
    sol = 0
    counter = 0
    for o_r in range(0, rows):
        for o_c in range(0, cols):
            counter += 1
            print(counter)
            r, c = start[0], start[1]
            directions = [
                (-1,0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ]
            d = 0
            seen = set()
            seen_rc = set()

            while True:
                if (r,c,d) in seen:
                    sol += 1
                    break
                seen.add((r,c,d))
                seen_rc.add((r,c))
                dr,dc = directions[d]
                new_r, new_c = r+dr, c+dc
                if new_r not in range(0, rows) or new_c not in range(0, cols):
                    print(o_r, o_c)
                    print(len(grid), len(grid[0]))
                    if grid[o_r][o_c] =='#':
                        p1 = len(seen_rc)
                    break
                if grid[new_r][new_c]=='#' or new_r==o_r and new_c==o_c:
                    d = (d+1)%4
                else:
                    r = new_r
                    c = new_c

        print(sol)
        
        
'''