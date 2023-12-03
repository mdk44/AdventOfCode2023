dia = 3

# input_file = 'Day' + str(dia) + '_Input.csv'
input_file = 'Day' + str(dia) + '_Test.csv'
# input_file = 'Day' + str(dia) + '_Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    print(line)