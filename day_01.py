from utils import get_input_lines
import re

def get_calibration_number_1(line):
    digit_1 = re.search('\\d', line)
    digit_2 = re.search('\\d', line[::-1])
    return int(f'{digit_1.group()}{digit_2.group()}')

def get_calibration_number_2(line):
    nums = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five' : 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    search = f"{'|'.join(nums.keys())}|{'|'.join(str(i) for i in range(1, 10))}"

    # Search forward
    digit_1 = re.search(search, line).group()
    digit_1 = digit_1 if digit_1.isdigit() else nums[digit_1]

    # Search backward
    digit_2 = re.search(search[::-1], line[::-1]).group()
    digit_2 = digit_2 if digit_2.isdigit() else nums[digit_2[::-1]]

    num = int(f'{digit_1}{digit_2}')
    return num

if __name__ == '__main__':
    input = get_input_lines(day=1)

    # Part 1
    print(sum(get_calibration_number_1(line) for line in input))

    # Part 2
    print(sum(get_calibration_number_2(line) for line in input))