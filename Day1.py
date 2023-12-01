dia = 1

input_file = 'Day' + str(dia) + '_Input.csv'
# input_file = 'Day' + str(dia) + '_Test.csv'
# input_file = 'Day' + str(dia) + '_Test2.csv'
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
digs = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

sum = 0
outp = ''
for line in lines:
    num1 = ''
    num2 = ''
    for i in range(0, len(line)):
        check3 = line[i : i + 3]
        check4 = line[i : i + 4]
        check5 = line[i : i + 5]
        if line[i] in ('0', '1',  '2', '3', '4', '5', '6', '7', '8', '9'):
            if num1 == '':
                num1 = line[i]
            else: num2 = line[i]
        elif check3 in digs:
            if num1 == '':
                num1 = digs[check3]
            else: num2 = digs[check3]
        elif check4 in digs:
            if num1 == '':
                num1 = digs[check4]
            else: num2 = digs[check4]
        elif check5 in digs:
            if num1 == '':
                num1 = digs[check5]
            else: num2 = digs[check5]
    if num2 == '':
        num2 = num1
    outp = str(num1) + str(num2)
    sum += int(outp)
    outp = ''
print('Part 2: ' + str(sum))