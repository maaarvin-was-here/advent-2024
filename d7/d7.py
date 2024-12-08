import os

def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            target = int(line.split(":")[0])
            nums = [int(x) for x in line.split(": ")[1].split(" ")]
            arr.append((target, nums))
    return arr


def calc(nums):
    if len(nums) == 1:
        return nums
    
    return(calc([nums[0] + nums[1]] + nums[2:]) + \
           calc([nums[0] * nums[1]] + nums[2:]))


def d6_1(inputs):
    valid_count = 0
    sol = 0
    for input in inputs:
        target, nums = input[0], input[1]

        all_possibilities = calc(nums)
        if target in all_possibilities:
            valid_count += 1
            sol += target
    
    # print(valid_count)
    # print(sol)
    return sol


def calc_2(nums):
    if len(nums) == 1:
        return nums
    
    return(calc_2([nums[0] + nums[1]] + nums[2:]) +                 # +
           calc_2([nums[0] * nums[1]] + nums[2:]) +                 # *
            calc_2([int(str(nums[0]) + str(nums[1]))] + nums[2:]))  # ||

def d6_2(inputs):
    valid_count = 0
    sol = 0
    for input in inputs:
        target, nums = input[0], input[1]
        all_possibilities = calc_2(nums)
        if target in all_possibilities:
            valid_count += 1
            sol += target
    
    return(sol)
    

if __name__ == '__main__':
    input_file = '{}/d7.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    sol_1 = d6_1(list)
    sol_2 = d6_2(list)

    print(sol_1)
    print(sol_2)

    # 414786463120 is too low
    

'''
def recursive_helper(target, nums):
    print("looking at nums")
    print(nums)
    if len(nums) == 1:
        if target == nums[0]:
            return True
        else:
            return False

    print(target, nums)
    cur = nums.pop(0)
    print(cur)

    if target >= cur:
        if target%cur == 0: # if the first element (or last before reversing) can cleanly divide into the target, we can test
            print("divisible")
            mul = recursive_helper(target//cur, nums)
            plus = recursive_helper(target-cur, nums)
            print(mul, plus)
            if mul or plus:
                return True
            # return recursive_helper(target//cur, nums) or recursive_helper(target-cur, nums)
        else:
            # print("not divisible")
            return recursive_helper(target-cur, nums)

            '''