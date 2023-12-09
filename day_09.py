from utils import get_input_lines


def get_history(line):
    history = [[int(x) for x in line.split()]]
    while set(history[-1]) != {0}:
        prev = history[-1]
        history.append([prev[i+1] - prev[i] for i in range(len(prev)-1)])
    return history

def get_next_value(line):
    history = get_history(line)
    value = 0
    for i in range(len(history)-2, -1, -1):
        value += history[i][-1]
    return value

def get_prev_value(line):
    history = get_history(line)
    value = 0
    for i in range(len(history)-2, -1, -1):
        value = history[i][0] - value
    return value
    


if __name__ == '__main__':
    input = get_input_lines(day=9)
    print('Part 1:', sum(get_next_value(line) for line in input))
    print('Part 2:', sum(get_prev_value(line) for line in input))