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

   

 

# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.

 

# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand.

# If these cards are different, the hand with the stronger first card is considered stronger.

# If the first card in each hand have the same label, however, then move on to considering the second card in each hand.

# If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

 

# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger.

# Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

 

# To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

 

# 32T3K 765

# T55J5 684

# KK677 28

# KTJJT 220

# QQQJA 483

# This example shows five hands; each hand is followed by its bid amount.

# Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand.

# Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

 

# So, the first step is to put the hands in order of strength:

 

# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.

# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.

# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

# Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5).

# So the total winnings in this example are 6440.

 

# Find the rank of every hand in your set. What are the total winnings?