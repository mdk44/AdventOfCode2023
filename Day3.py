import re

dia = 3

input_file = 'Day' + str(dia) + '_Input.csv'
# input_file = 'Day' + str(dia) + '_Test.csv'
# input_file = 'Day' + str(dia) + '_Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def find_nums(inp):
    nums = re.findall(r"\d+", inp)
    return nums

def find_search_radius(i, num, beg):
    if i == 0:
        y1 = 0
    else:
        y1 = i - 1
    x1 = max(0, lines[i].find(num, beg) - 1)
    if i == len(lines) - 1:
        y2 = len(lines) - 1
    else:
        y2 = i + 1
    x2 = min(len(lines[i]) - 1, lines[i].find(num, beg) + len(num))
    return y1, x1, y2, x2

def compare_nums(i):
    beg = 0
    sum = 0
    nums = find_nums(lines[i])
    for j in range(0, len(nums)):
        succ = 0
        y1, x1, y2, x2 = find_search_radius(i, nums[j], beg)
        beg = x2
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                try:
                    if lines[y][x] not in ('.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        succ = 1
                except:
                    print(y, x)
        if succ == 1:
            sum += int(nums[j])
    return sum

def count_nums(inp):
    nums = find_nums(inp)
    if len(nums) != len(list(set(nums))):
        print(nums)

# Part 1
cum_sum = 0
for i in range(0, len(lines)):
    cum_sum += compare_nums(i)
    
print("Part 1: " + str(cum_sum))