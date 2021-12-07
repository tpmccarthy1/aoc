import sys


def find_minimum(crabs):
    crabs.sort()
    # get max
    max = crabs[len(crabs) - 1]
    # calc sum from min to max
    min_total = sum(crabs)
    for i in range(0, max, 1):
        temp = 0
        for num in crabs:
            temp += abs(i - num)
        if temp < min_total:
            min_total = temp

    return min_total


def main():
    with open(sys.argv[1]) as f:
        crabs = f.readline().split()
    return find_minimum(crabs)

if __name__ == '__main__':
    main()
