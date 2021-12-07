import sys


def find_minimum(crabs):
    crabs.sort()
    # get max
    max = crabs[len(crabs) - 1]
    # calc sum from min to max
    min_total = sys.maxsize
    totals = {}
    for i in range(0, max, 1):
        temp = 0
        for num in crabs:             
            diff = abs(num - i)
            total = sequence(abs(diff))
            temp += total
        totals[i] = temp
        if temp < min_total:
            min_total = temp
    print(min(totals.values()))
    return min_total

def sequence(num, seen={}):
    if (num == 0):
        return 0
    if num not in seen:
        seen[num] = num + sequence(num-1, seen)
    return seen[num]


def main():
    with open(sys.argv[1]) as f:
        crabs = list(map(int, f.readline().split(',')))

    return find_minimum(crabs)


if __name__ == '__main__':
    print(main())
