def read_file_to_memory(path):
    with open(path) as f:
        content = [line.rstrip() for line in f]
    return content

def parse_policy(policy):
    range = policy.split(' ')[0].split('-')
    return {
        'range': [int(range[0]), int(range[1])],
        'char': policy.split(' ')[1].strip(':')
    }


def test_password(policy, password):
    char = policy.get('char')
    return bool(password[policy.get('range')[0]-1] == char) ^ bool(password[policy.get('range')[1]-1] == char)



def main():
    # Read the file into memory for proccessing
    file_content = read_file_to_memory('aoc2input.txt')
    count = 0
    for line in file_content:
        policy = parse_policy(line)
        password = line.split(':')[1].strip()
        if test_password(policy, password):
            count += 1
    print(count)

    print(sum([(2.5*5.5), (5*5.5), (2.5*5.5), (2.5*5)]))


if __name__ == "__main__":
    main()
