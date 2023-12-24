import re
from parse import *
from collections import defaultdict
from utils import get_input_lines
import itertools


transitions = [
    'seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location'
]
maps = defaultdict(dict)

def make_maps(input):
    vals = parse('seeds: {seeds}', input[0])
    seeds = [int(i) for i in vals['seeds'].split()]

    for i in range(2, len(input)):
        line = input[i]
        vals = parse('{from}-to-{to} map:', line)
        if vals:
            map_name = f'{vals["from"]}-{vals["to"]}'
            i += 1
            while i < len(input) and (line := input[i]) != '':
                to_start, from_start, range_len = (int(x) for x in line.split())
                maps[map_name][from_start] = (to_start, range_len)
                i += 1

    return seeds

def get_direct_to_num(from_num, from_name, to_name):
    mapping = maps[f'{from_name}-{to_name}']
    for from_key in sorted(mapping.keys()):
        to_key, range_len = mapping[from_key]
        # Range hit
        if from_key <= from_num < from_key + range_len:
            return to_key + from_num - from_key
        # From num is not mapped
        elif from_key > from_num:
            break
    # Default mapping
    return from_num

def get_chained_to_num(from_num, from_name, to_name):
    from_i = transitions.index(from_name)
    to_i = transitions.index(to_name)
    if abs(to_i - from_i) == 1:
        return get_direct_to_num(from_num, from_name, to_name)
    next_name = transitions[from_i + 1]
    next_num = get_direct_to_num(from_num, from_name, next_name)
    return get_chained_to_num(next_num, next_name, to_name)
   
def get_reverse_direct_to_num(to_num, to_name, from_name):
    mapping = maps[f'{from_name}-{to_name}']
    for from_key in mapping.keys():
        to_key, range_len = mapping[from_key]
        # Range hit
        if to_key <= to_num < to_key + range_len:
            return from_key + to_num - to_key
    # Default mapping
    return to_num

def get_reverse_chained_to_num(to_num, to_name, from_name):
    from_i = transitions.index(from_name)
    to_i = transitions.index(to_name)
    if abs(to_i - from_i) == 1:
        return get_reverse_direct_to_num(to_num, to_name, from_name)
    prev_name = transitions[to_i - 1]
    prev_num = get_reverse_direct_to_num(to_num, to_name, prev_name)
    return get_reverse_chained_to_num(prev_num, prev_name, from_name)

def part_1(input):
    seeds = make_maps(input)
    return min(get_chained_to_num(seed_num, 'seed', 'location') for seed_num in seeds)

def part_2(input):
    seeds = make_maps(input)
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))
    
    
    location_num = 0
    while True:
        print(location_num)
        seed_num = get_reverse_chained_to_num(location_num, 'location', 'seed')
        for r in seed_ranges:
            if seed_num in r:
                return location_num
        location_num += 1
            


if __name__ == '__main__':
    vals = parse('day_{day}.py', __file__)
    input = get_input_lines(day=int(vals['day']))

    print('Part 1:', part_1(input))
    print('Part 2:', part_2(input))
    