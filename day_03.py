import re
from collections import defaultdict
from utils import get_input_lines


class Number:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def is_part_number(self, schematic):
        return is_number_adjacent_to_symbol(self, schematic)
    
    def get_adjacent_gears(self, schematic):
        self.adjacent_gears = find_adjacent_gears(self, schematic)        


def find_numbers(schematic):
    numbers = []
    for row, line in enumerate(schematic):
        tokens = re.split('[^\d]', line)
        for i, token in enumerate(tokens):
            if token.isdigit():
                col = sum(len(t) + 1 for t in tokens[:i])
                numbers.append(Number(row, col, int(token)))
    return numbers


def is_number_adjacent_to_symbol(num, schematic):
    max_row = len(schematic) - 1

    rows_to_check = (
        [0, 1] if num.row == 0 else 
        [max_row - 1, max_row] if num.row == max_row else
        [num.row - 1, num.row, num.row + 1]
    )
    cols_to_check = range(max(0, num.col-1), min(num.col+len(str(num.value))+1, len(schematic[0])))

    for row in rows_to_check:
        for col in cols_to_check:
            c = schematic[row][col]
            if c != '.' and not c.isdigit():
                return True
    return False


def find_adjacent_gears(num, schematic):
    max_row = len(schematic) - 1

    rows_to_check = (
        [0, 1] if num.row == 0 else 
        [max_row - 1, max_row] if num.row == max_row else
        [num.row - 1, num.row, num.row + 1]
    )
    cols_to_check = range(max(0, num.col-1), min(num.col+len(str(num.value))+1, len(schematic[0])))

    gears = []
    for row in rows_to_check:
        for col in cols_to_check:
            c = schematic[row][col]
            if c == '*':
                gears.append((row, col))
    return gears


if __name__ == '__main__':
    schematic = get_input_lines(day=3)
    numbers = find_numbers(schematic)
    print('Part 1:', sum(num.value for num in numbers if num.is_part_number(schematic)))

    gear_parts = defaultdict(list)
    for number in numbers:
        number.get_adjacent_gears(schematic)
        for gear in number.adjacent_gears:
            gear_parts[gear].append(number.value)
    
    gear_ratio_sum = 0
    for parts in gear_parts.values():
        if len(parts) == 2:
            gear_ratio = parts[0] * parts[1]
            gear_ratio_sum += gear_ratio
    print('Part 2:', gear_ratio_sum)