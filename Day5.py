dia = 5
test = 1

if test == 1:
    f = 'Test'
else:
    f = 'Input'
input_file = 'Day' + str(dia) + '_' + f + '.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
