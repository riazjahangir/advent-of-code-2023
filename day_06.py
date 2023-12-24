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

            


if __name__ == '__main__':
    races = [
        (40, 233),
        (82, 1011),
        (84, 1110),
        (92, 1487)
    ]
    
    # races = [
    #     (7, 9),
    #     (15, 40),
    #     (30, 200)
    # ]

    print('Part 1:', part_1(races))
    