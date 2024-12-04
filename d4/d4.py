import os

def process(f):
    input_lines = []
    with open(f, "r") as file:
        for line in file:
            input_lines.append(line)
        return input_lines


if __name__ == '__main__':
    input_file = '{}/d4_test.txt'.format(os.path.basename(__file__).split(".")[0])
    # print(input_file)
    list = process(input_file)
    print(list)
    
    # print(d3_1(list))
    # print(d3_2(list))
