import os

DEBUG = False

def dbpr(x):
    if DEBUG:
        print(x)
    
def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            temp = []
            for char in line:
                if char != '\n':
                    if char != '.':
                        temp.append(int(char))
                    else:
                        temp.append(char)
            arr.append(temp)
    return arr


def d10_1(grid):
    def explore(coord):
        found = set()
        q = [coord]

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            cur = q.pop()
            cur_r, cur_c = cur[0], cur[1]
            cur_val = grid[cur_r][cur_c]
            if cur_val == 9:
                # print("found end")
                found.add((cur_r, cur_c))
            
            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc
                if new_r in range(0, rows) and \
                    new_c in range(0, cols) and \
                        grid[new_r][new_c] == cur_val + 1:
                    q.append((new_r, new_c))
                    
        

        return len(found)


    rows, cols = len(grid), len(grid[0])

    sol = 0
    trailheads = []
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 0:
                trailheads.append((i,j))
    
    for trailhead in trailheads:
        sol += explore(trailhead)

    return sol


def d10_2(grid):
    def explore(coord):
        found = []
        q = [coord]

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            cur = q.pop()
            cur_r, cur_c = cur[0], cur[1]
            cur_val = grid[cur_r][cur_c]
            if cur_val == 9:
                # print("found end")
                found.append((cur_r, cur_c))
            
            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc
                if new_r in range(0, rows) and \
                    new_c in range(0, cols) and \
                        grid[new_r][new_c] == cur_val + 1:
                    q.append((new_r, new_c))
                    
        

        return len(found)


    rows, cols = len(grid), len(grid[0])

    sol = 0
    trailheads = []
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 0:
                trailheads.append((i,j))
    
    for trailhead in trailheads:
        sol += explore(trailhead)

    return sol


if __name__ == '__main__':
    input_file = '{}/d10.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    # dbpr(list)

    p1 = d10_1(list)
    p2 = d10_2(list)

    print(p1)
    print(p2)