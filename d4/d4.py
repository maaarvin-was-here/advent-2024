import os

def process(f):
    input_lines = []
    with open(f, "r") as file:
        for line in file:
            arr = []
            for char in line:
                if char != '\n':
                    arr.append(char)
            input_lines.append(arr)
        return input_lines

def d4_1(grid):
    sol = 0
    directions = [
        (-1, -1),   # up left
        (-1, 0),    # up
        (-1, 1),    # up right
        (0, -1),    # left
        (0, 1),     # right
        (1, -1),    # down left
        (1, 0),     # down
        (1, 1)      # down right
    ]

    def search_x(coord):
        counter = 0
        r = coord[0]
        c = coord[1]
        for dr, dc in directions:
            new_r = r + (dr * 3)
            new_c = c + (dc * 3)
            if new_r in range(0, rows) and \
                new_c in range(0, cols):
                    string = ''
                    for i in range(0, 4):
                        string += grid[r + (dr * i)][c + (dc * i)]
                    if string == 'XMAS':
                        counter += 1
        
        return counter

    rows, cols = len(grid), len(grid[0])

    # i, j -> i pertains to verticality, j pertains to horizontal. top left is the origin
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 'X':
                sol += search_x((i,j))
    
    return sol


# checks if a potential X with the 'A' in the center is valid on the grid bounds
def is_valid_a(grid, coord):
    rows, cols = len(grid), len(grid[0])
    r = coord[0]
    c = coord[1]
    directions = [
            (-1, -1),   # up left
            (-1, 1),    # up right
            (1, -1),    # down left
            (1, 1)      # down right
        ]

    for dr, dc in directions:
        if r + dr not in range(0, rows) or \
            c + dc not in range(0, cols): 
                return False
    
    return True


def d4_2(grid):

    # searches in opposite corners of the 'A' and checks if there is exactly 1 'M' and exactly 1 'S' for each
    # pair of opposing diagonals
    def search_a(coord):
        r = coord[0]
        c = coord[1]

        directions = [
            [
                (-1, -1),   # up left
                (1, 1)      # down right
            ],
            [
                (-1, 1),    # up right
                (1, -1),    # down left
            ]
        ]

        for pair in directions:
            letter_set = {
                'S':0,
                'M':0
            }
            for dr, dc in pair:
                new_r = r + dr
                new_c = c + dc
                if grid[new_r][new_c] not in letter_set:
                    return 0
                letter_set[grid[new_r][new_c]] += 1
            if letter_set['S'] != 1 or letter_set['M'] != 1:
                return 0

        return 1
        

    rows, cols = len(grid), len(grid[0])

    # i, j -> i pertains to verticality, j pertains to horizontal. top left is the origin
    sol = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 'A':
                if is_valid_a(grid, (i, j)):
                    sol += search_a((i,j))
    
    return sol


if __name__ == '__main__':
    input_file = '{}/d4.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)
    
    
    print(d4_1(list))
    print(d4_2(list))


'''
i thought it could curve like bfs/recursion... didn't realize only XMAS in straight lines were valid

def search_for_words(cur, string, visited):
        sum = 0
        r = cur[0]
        c = cur[1]
        print(" ")
        print("looking at " + string)
        if string == 'XMAS':
            print("match!")
            return 1

        if string != 'XMAS'[0:len(string)]:
            print(string + " is not a match!")
            return 0

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if new_r in range(0, rows) and \
                new_c in range(0, cols) and\
                (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    print("going to " + str(new_r) + ", " + str(new_c))
                    sum += search_for_words((new_r, new_c), string + grid[new_r][new_c], visited)
                    print("sum is now " + str(sum))
        
        print("exiting " + string + " with sum: " + str(sum))
        print(sum)
        return sum
    
    '''