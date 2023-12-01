dia = 1

# input_file = 'Day' + str(dia) + '_Input.csv'
# input_file = 'Day' + str(dia) + '_Test.csv'
input_file = 'Day' + str(dia) + '_Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Part 1
sum = 0
outp = ''
for line in lines:
    num1 = ''
    num2 = ''
    for i in range(0, len(line)):
        if line[i] in ('0', '1',  '2', '3', '4', '5', '6', '7', '8', '9'):
            if num1 == '':
                num1 = line[i]
            else: num2 = line[i]
    if num2 == '':
        num2 = num1
    outp = num1 + num2
    sum += int(outp)
    outp = ''
print('Part 1: ' + str(sum))

# Part 2
