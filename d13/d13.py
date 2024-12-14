import os
from sympy import *
import re


DEBUG = False

def dbpr(x):
    if DEBUG:
        print(x)
    
def process(f):
    arr = []
    with open(f, "r") as file:
        content = file.read()
        machines = content.split('\n\n')
        for m in machines:
            temp = []
            x = m.split('\n')
            for line in x:
                nums = re.findall(r'\d+', line)
                # print(nums)
                if nums:
                    temp.append((int(nums[0]), int(nums[1])))
            arr.append(temp)
    return arr




def d13_1(machines):
    ans = 0
    counter = 0
    for machine in machines:
        counter += 1
        # print(int(100*counter/len(machines)))
        button_A = machine[0]
        button_B = machine[1]
        prize_coord = machine[2]
        # print(prize_coord)

        Ax,Ay = button_A[0], button_A[1]
        Bx,By = button_B[0], button_B[1]
        Px,Py = prize_coord[0], prize_coord[1]

        slopeA = Ay/Ax
        slopeB = By/Bx

        # print(slopeA)
        # print(slopeB)
        
        # always have A intersect origin (for ease of calc)
        
        # equation A: y = Ay/Ax * x
        # equation B: y = Py + (By/Bx)*(x-Px)

        # (Py - slopeB*Px)/(slopeA-slopeB)

        # x = (Py - slopeB*Px)/(slopeA-slopeB)
        # y = slopeA * x

        x = (Py * Bx - Px * By) / (Ay * Bx - Ax * By)
        y = -((Py * Ax - Px * Ay) / (Ay * Bx - Ax * By))

        # x,y = symbols('x y')
        # s = linsolve([
        #     x*(Ay/Ax) - y,
        #     Py + (By/Bx)*(x-Px) - y
        # ], (x,y))
        # # print(s)


        # sol = s.args[0]

        sol = (x,y)
        # print(sol)
        
        if x.is_integer() and y.is_integer():
            pA = int(x)
            pB = int(y)

            ans += pA * 3
            ans += pB

    return ans


def d13_2(machines):
    offset = 10000000000000
    
    ans = 0
    counter = 0
    for machine in machines:
        counter += 1
        # print(int(100*counter/len(machines)))
        button_A = machine[0]
        button_B = machine[1]
        prize_coord = machine[2]
        # print(prize_coord)

        Ax,Ay = button_A[0], button_A[1]
        Bx,By = button_B[0], button_B[1]
        Px,Py = prize_coord[0] + offset, prize_coord[1] + offset

        slopeA = Ay/Ax
        slopeB = By/Bx

        # print(slopeA)
        # print(slopeB)
        
        # always have A intersect origin (for ease of calc)
        
        # equation A: y = Ay/Ax * x
        # equation B: y = Py + (By/Bx)*(x-Px)

        # (Py - slopeB*Px)/(slopeA-slopeB)

        # x = (Py - slopeB*Px)/(slopeA-slopeB)
        # y = slopeA * x

        x = (Py * Bx - Px * By) / (Ay * Bx - Ax * By)
        y = -((Py * Ax - Px * Ay) / (Ay * Bx - Ax * By))

        # x,y = symbols('x y')
        # s = linsolve([
        #     x*(Ay/Ax) - y,
        #     Py + (By/Bx)*(x-Px) - y
        # ], (x,y))
        # # print(s)


        # sol = s.args[0]

        sol = (x,y)
        # print(sol)
        
        if x.is_integer() and y.is_integer():
            pA = int(x)
            pB = int(y)
            ans += pA * 3
            ans += pB

    return ans


if __name__ == '__main__':
    input_file = '{}/d13.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    # for i in list:
        # print(i)

    s1 = d13_1(list)
    s2 = d13_2(list)

    # s1, s2 = d12_1(list)
    print(s1)
    print(s2)
    # print(s2)

    # 21624 too low