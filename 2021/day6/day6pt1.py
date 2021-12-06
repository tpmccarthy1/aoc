import sys


def reproduce(fish_status_map):
    temp_fish = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}
    for key in fish_status_map.keys():
        value = fish_status_map.get(key)
        # remove fish from current position
        fish_status_map[key] -= value
        # create new fish if 0
        if key == 0:
            temp_fish[8] += value
            temp_fish[6] += value
        else:
            temp_fish[key-1] += value

    for key in temp_fish.keys():
        fish_status_map[key] += temp_fish.get(key)


def main():
    # the number of days to run the simulation
    num_days = 80

    fish_status_map = {
        8: 0,
        7: 0,
        6: 0,
        5: 0,
        4: 0,
        3: 0,
        2: 0,
        1: 0,
        0: 0
    }

    with open(sys.argv[1]) as f:
        for time in [list(map(int, line.strip().split(','))) for line in f][0]:
            fish_status_map[time] += 1

    # run simulation for 80 days
    for i in range(0, num_days, 1):
        reproduce(fish_status_map)

    return sum(fish_status_map.values())


if __name__ == '__main__':
    print(main())
