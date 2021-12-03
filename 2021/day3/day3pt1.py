import sys


def read_file_to_memory(path):
    with open(path) as f:
        content = [list(map(int, list(line.strip()))) for line in f]
    return content


def parse(bits, is_gamma):
    length = len(bits[0])
    result = []
    pos = 0
    # gamma
    while (pos < length):
        high = 0
        low = 0
        for row in bits:
            if (row[pos] == 1):
                high += 1
            else:
                low += 1
        if (high > low):
            result.append(1 if is_gamma else 0)
        else:
            result.append(0 if is_gamma else 1)
        pos += 1
    return result


def main():
    filename = sys.argv[1]

    bits = read_file_to_memory(filename)

    gamma = parse(bits, True)
    epsilon = parse(bits, False)
    
    g_str = ''
    gamma_dec = int(g_str.join(list(map(str, gamma))), 2)
    epsilon_dec = int(g_str.join(list(map(str, epsilon))), 2)
    
    print(gamma_dec * epsilon_dec)


if __name__ == "__main__":
    main()
