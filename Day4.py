import re

dia = 4

# input_file = 'Day' + str(dia) + '_Input.csv'
input_file = 'Day' + str(dia) + '_Test.csv'
# input_file = 'Day' + str(dia) + '_Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def my_nums(inp):
    mynums = []
    inp = inp.split(' | ')[0]
    inp = inp.split(': ')[1]
    nums = re.findall(r"\d+", inp)
    for i in range(0, len(nums)):
        mynums.append(int(nums[i]))
    return mynums

def winning_nums(inp):
    wnums = []
    inp = inp.split(' | ')[1]
    nums = re.findall(r"\d+", inp)
    for i in range(0, len(nums)):
        wnums.append(int(nums[i]))
    return wnums

def check_nums(inp):
    cnt = 0
    mynums = my_nums(inp)
    wnums = winning_nums(inp)
    for m in mynums:
        if m in wnums:
            cnt += 1
    score = int(2 ** (cnt - 1))
    return score, cnt

# Part 1
cum_sum = 0
for line in lines:
    cum_sum += check_nums(line)[0]
print("Part 1: " + str(cum_sum))

# Part 2
cards = {}
for line in lines:
    card = line.split(':')[0]
    num = re.findall(r"\d+", card)
    cards['Card ' + num[0]] = 1

for x in range(0, len(lines)):
    cnt = check_nums(lines[x])[1]
    for i in range(x + 2, min(x + cnt + 2, len(lines))):
        cards['Card ' + str(i)] += cards['Card ' + str(x + 1)]
print("Part 2: " + str(sum(cards.values())))