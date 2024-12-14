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
                    temp.append(char)
            arr.append(temp)
    return arr


def d12_1(grid):
    rows, cols = len(grid), len(grid[0])
    global_visited = set()

    def bfs(coord, val):
        local_visited = set()
        seen_edges = set()

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        area = 0

        # calculate area
        q = [coord]
        while q:
            # print(q)
            cur = q.pop(0)
            cur_r, cur_c = cur[0], cur[1]

            global_visited.add(cur)
            if cur not in local_visited:
                area += 1
            local_visited.add(cur)

            # print("out of loop")

            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc
                if new_r in range(0, rows) and \
                    new_c in range(0, cols) and \
                        (new_r, new_c) not in local_visited and \
                            grid[new_r][new_c] == val:
                    if (new_r, new_c) not in q:
                    # print("appending " + str((new_r, new_c)))

                
                        q.append((new_r, new_c))
                    seen_edges.add(((cur_r, cur_c), (new_r, new_c)))
            
        
        # calculate perimeter

        perimeter = 0

        for pr, pc in local_visited:
            perimeter += 4
            # print(pr, pc)
            for dr, dc in dirs:
                if ((pr, pc), (pr+dr,pc+dc)) in seen_edges or \
                    ((pr+dr,pc+dc),(pr,pc)) in seen_edges:
                    perimeter -=1
        

        # find corners

        cdirs = [
            (-1,0),     # up
            (0,1),      # right
            (1,0),      # down
            (0,-1)      # left
        ]

        corners = 0

        for cr, cc in local_visited:
            v = grid[cr][cc]
            # print(v)
            n = []
            # print(cr,cc)
            for dr, dc in cdirs:
                nr = cr+dr if cr+dr in range(0, rows) else ''
                nc = cc+dc if cc+dc in range(0, cols) else ''
                n.append((nr,nc))
            # print(n)
            for i in range(0, len(n)):
                j = (i+1)%4
                c1,c2 = n[i],n[j]
                c1r,c1c,c2r,c2c = c1[0],c1[1],c2[0],c2[1]
                if c1r == '' or c1c == '':
                    c1 = ''
                else:
                    c1 = grid[c1r][c1c]
                if c2r == '' or c2c == '':
                    c2 = ''
                else:
                    c2 = grid[c2r][c2c]
                
                diag_r = cdirs[i][0] + cdirs[j][0]
                diag_c = cdirs[i][1] + cdirs[j][1]

                # check outer corners
                if c1 != v and c2 != v:
                    corners += 1

                if cr + diag_r in range(0, rows) and cc + diag_c in range(0, cols):
                    diag = grid[cr + diag_r][cc+diag_c]
                else:
                    diag = ''
                
                if c1 == v and c2 == v and diag != v: # and #diagonal not v:
                    corners += 1

                
                
                
        print(corners)
        # print(seen_edges)
        return(area * perimeter, area * corners)


        

    sol1, sol2 = 0, 0
    for r in range(0, rows):
        for c in range(0, cols):
            val = grid[r][c]
            if (r,c) not in global_visited:
                print("cur looking at: " + val)
                sol = bfs((r,c), val)
                sol1 += sol[0]
                sol2 += sol[1]

    
    return sol1, sol2



if __name__ == '__main__':
    input_file = '{}/d12.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    # print(list)

    s1, s2 = d12_1(list)
    print(s1)
    print(s2)