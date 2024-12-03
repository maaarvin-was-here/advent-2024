import os
import re


def process(f):
    input_lines = []
    with open(f, "r") as file:
        for line in file:
            input_lines.append(line)
        return input_lines
    

def d3_1(lines):
    sol = 0
    for line in lines:
        for match in re.finditer(r"mul[\(]\d+[\,]\d+[\)]", line):
            eq = match.group(0)
            r1 = eq.split(",")[0].split("(")[1]
            r2 = eq.split(",")[1][:-1]
            sol += (int(r1) * int(r2))
    return sol


def d3_2(lines):
    sol = 0
    enabled = True
    for line in lines:
        for match in re.finditer(r"mul[\(]\d+[\,]\d+[\)]|don[\']t[\(][\)]|do[\(][\)]", line):
            eq = match.group(0)
            if eq == 'do()':
                enabled = True
            elif eq == 'don\'t()':
                enabled = False
            else:
                if(enabled):
                    r1 = eq.split(",")[0].split("(")[1]
                    r2 = eq.split(",")[1][:-1]
                    sol += (int(r1) * int(r2))
    return sol

if __name__ == '__main__':
    input_file = '{}/d3.txt'.format(os.path.basename(__file__).split(".")[0])
    print(input_file)
    list = process(input_file)
    
    # print(d3_1(list))
    print(d3_2(list))
