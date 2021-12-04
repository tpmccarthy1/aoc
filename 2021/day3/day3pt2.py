import sys


def read_file_to_memory(path):
    with open(path) as f:
        content = [list(map(int, list(line.strip()))) for line in f]
    return content


def parse(bits, oxygen):
    length = len(bits[0])
    pos = 0
    # gamma
    while (pos < length and len(bits) > 1):
        high = 0
        low = 0
        for row in bits:
            if (row[pos] == 1):
                high += 1
            else:
                low += 1
        if (high < low):
            bits = list(filter(lambda a: a[pos] == 0 if oxygen else a[pos] == 1, bits))
        else:
             bits = list(filter(lambda a: a[pos] == 1 if oxygen else a[pos] == 0, bits))
        pos += 1

    return bits


def main():
    filename = sys.argv[1]

    bits = read_file_to_memory(filename)

    gamma = epsilon = ""
    for n in range(len(bits[0])):
        col = [row[n] for row in bits]
        gamma += max(set(col), key=col.count)
        epsilon += min(set(col), key=col.count)
    power_consumption = int(gamma, 2) * int(epsilon, 2)
    print(f"Part 1: {power_consumption}")


if __name__ == "__main__":
    main()
