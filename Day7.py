dia = 7
test = 1

if test == 1: f = 'Test'
else: f = 'Input'
input_file = 'Day' + str(dia) + '_' + f + '.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

cards = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

 

hands = {
    '5 of a Kind': 7,
    '4 of a Kind': 6,
    'Full House': 5,
    '3 of a Kind': 4,
    '2 Pair': 3,
    '1 Pair': 2,
    'High Card': 1
}

def score_hand(inp):
    hand = {}
    for i in range(0, 5):
        card = inp.split(' ')[0][i]
        if card in hand:
            hand[card] += 1
        else:
            hand[card] = 1
    if 5 in hand.values(): return '5 of a Kind'
    elif 4 in hand.values(): return '4 of a Kind'
    elif 3 in hand.values() and 2 in hand.values(): return 'Full House'
    elif 3 in hand.values(): return '3 of a Kind'
    elif sum(1 for v in hand.values() if v == 2) == 2: return '2 Pair'
    elif 2 in hand.values(): return '1 Pair'
    else: return 'High Card'
 
def score_cards(inp):
    hand = []
    for i in range(0, 5):
        hand.append(cards[inp.split(' ')[0][i]])
    print(hand)

def rank_cards(inp):
    res = {}
    for h in range(0, len(inp)):
        c = inp[h]
        res[h + 1] = (c.split(' ')[0], hands[score_hand(c)], int(c.split(' ')[1]))
    print(res)

for line in lines:
    print(score_hand(line))
    score_cards(line)

rank_cards(lines)