import functools

def get_ways_to_win(race):
    ways = []
    # t = race time
    t, distance_record = race
    # b = time spent holding button
    # t - b = time spent moving
    # b * (t - b) = distance moved
    for b in range(1, t + 1):
        if b * (t - b) > distance_record:
            ways.append(b)

    return ways

def part_1(races):
    num_ways_to_win = [len(get_ways_to_win(race)) for race in races]
    return functools.reduce(lambda a, b: a * b, num_ways_to_win)


def part_2(race):
    return len(get_ways_to_win(race))
            


if __name__ == '__main__':
    race = (40828492, 233101111101487)

    # race = (71530, 940200)
    
    print('Part 2:', part_2(race))
    