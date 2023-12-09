import re
from parse import *
from collections import defaultdict
from utils import get_input_lines

def parse_card(card):
    vals = parse('Card {id:4d}: {winning} | {mine}', card)
    winning_nums = [int(i) for i in vals['winning'].split() if i]
    my_nums = [int(i) for i in vals['mine'].split() if i]
    return vals['id'], winning_nums, my_nums
 
def get_num_matches(winning_nums, my_nums):
    return len(set(winning_nums).intersection(set(my_nums)))

def get_points(card):
    _, winning_nums, my_nums = parse_card(card)
    matches = get_num_matches(winning_nums, my_nums)
    if matches:
        return 2 ** (matches - 1)
    return 0

if __name__ == '__main__':
    vals = parse('day_{day}.py', __file__)
    input = get_input_lines(day=int(vals['day']))

    print('Part 1:', sum(get_points(card) for card in input))

    copies = defaultdict(lambda: 1)
    count = 0
    for card in input:
        card_id, winning_nums, my_nums = parse_card(card)
        for copy_i in range(copies[card_id]):
            count += 1
            if num_matches := get_num_matches(winning_nums, my_nums):
                for i in range(1, num_matches + 1):
                    copies[card_id + i] += 1
    
    print('Part 2:', count)