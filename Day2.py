import re

dia = 2

input_file = 'Day' + str(dia) + '_Input.csv'
# input_file = 'Day' + str(dia) + '_Test.csv'
# input_file = 'Day' + str(dia) + '_Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def score(line):
    red = 0
    green = 0
    blue = 0
    game = int(line[5 : line.find(':', 0)])
    round = line.split('; ')
    round[0] = round[0][round[0].find(':', 0) + 2 : len(round[0])]
    for i in range(0, len(round)):
        r = round[i].split(', ')
        for j in range(0, len(r)):
            cubes = r[j].split(' ')
            if cubes[1] == 'red':
                if int(cubes[0]) > red:
                    red = int(cubes[0])
            elif cubes[1] == 'green':
                if int(cubes[0]) > green:
                   green = int(cubes[0])
            elif cubes[1] == 'blue':
                if int(cubes[0]) > blue:
                   blue = int(cubes[0])
    if red <= 12 and green <= 13 and blue <= 14:
        return game
    else:
        return 0

# Part 1
sum = 0
for line in lines:
    sum += score(line)
print("Part 1: " + str(sum))