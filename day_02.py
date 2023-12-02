from utils import get_input_lines
from parse import *
from collections import defaultdict


def id_if_possible(game, red=12, green=13, blue=14):
    vals = parse('Game {id:d}: {sets}', game)
    if sets_are_possible(vals['sets'], red, green, blue):
        return vals['id']
    return 0


# Sets are like '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
def sets_are_possible(sets, red, green, blue):
    return all([
        set_is_possible(game_set.strip(), red, green, blue) for game_set in sets.split(';')
    ])


def set_is_possible(game_set, red, green, blue):
    cubes = get_cubes(game_set)
    return all([
        cubes.get('red', 0) <= red,
        cubes.get('green', 0) <= green,
        cubes.get('blue', 0) <= blue,
    ])
    

# A result is like '3 blue, 4 red'
# Return { 'blue': 3, 'red': 4 }
def get_cubes(result):
    cubes = {}
    colors = result.split(',')
    for color in colors:
        num, col = color.split()
        cubes[col] = int(num)
    return cubes


# Part 2
def get_power(min_required):
    product = 1
    for num in min_required.values():
        product *= num
    return product


# Return { 'blue': 3, 'red': 4 }
def get_min_required_cubes(game):
    vals = parse('Game {id:d}: {sets}', game)
    sets = vals['sets'].split(';')
    min_cubes = defaultdict(int)
    for game_set in sets:
        cubes = get_cubes(game_set)
        for color, num in cubes.items():
            min_cubes[color] = max(min_cubes[color], num)
    return min_cubes


if __name__ == '__main__':
    input = get_input_lines(day=2)
    print(sum(id_if_possible(line) for line in input))
    print(sum(get_power(get_min_required_cubes(line)) for line in input))
