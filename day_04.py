import re
from parse import *
from collections import defaultdict
from utils import get_input_lines

def get_points(card):
    vals = parse('Card {id:4d}: {winning} | {mine}', card)
    winning_nums = [int(i) for i in vals['winning'].split() if i]
    my_nums = [int(i) for i in vals['mine'].split() if i]
    matches = set(winning_nums).intersection(set(my_nums))
    if matches:
        return 2 ** (len(matches) - 1)
    return 0

if __name__ == '__main__':
    input = get_input_lines(day=4)
    print('Part 1:', sum(get_points(card) for card in input))