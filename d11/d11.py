import os
import functools

DEBUG = False

def dbpr(x):
    if DEBUG:
        print(x)
    
def process(f):
    arr = []
    with open(f, "r") as file:
        for line in file:
            nums = line.split(" ")
            for n in nums:
                arr.append(int(n))         
    return arr


def blink(nums):
    dbpr("blinking")
    p = 0
    dbpr(len(nums))

    while p < len(nums):
        print(100 * p/len(nums))
        dbpr("in da loop")
        if nums[p] == 0:
            nums[p] = 1
        elif len(str(nums[p]))%2==0:
            middle = len(str(nums[p]))//2
            dbpr(middle)
            dbpr("x")
            dbpr(nums[len(str(nums[p]))//2:])
            t1 = int(str(nums[p])[:middle])
            t2 = int(str(nums[p])[middle:])
            dbpr((t1, t2))
            nums[p] = t1
            nums.insert(p+1, t2)
            p += 1
        else:
            dbpr("HERE")
            nums[p] *= 2024
        p += 1
        dbpr(nums)
    
    return nums



def d11_1(starting_nums):
    cur = starting_nums
    for i in range(0, 25):
        cur = blink(cur)
    
    sol = len(cur)
    return(sol)



def d11_2(starting_nums, target):
    @functools.cache
    def blink2(num, counter):
        dbpr(counter)
        if counter == target:
            return 1
        if num == 0:
            return blink2(1, counter+1)
        elif len(str(num))%2==0:
            dbpr(("num", num))
            middle = len(str(num))//2
            # dbpr(middle)
            t1 = int(str(num)[:middle])
            t2 = int(str(num)[middle:])
            dbpr((t1, t2))
            return (blink2(t1, counter+1) + blink2(t2, counter+1))
        else:
            return blink2(num * 2024, counter+1)

    sol = 0
    for num in starting_nums:
        dbpr(num)
        dbpr("SHOULD BE")
        sol += blink2(num, 0)
    
    return sol


if __name__ == '__main__':
    input_file = '{}/d11.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    dbpr(list)

    p1 = d11_2(list, 25)
    p2 = d11_2(list, 75)

    print(p1)
    print(p2)