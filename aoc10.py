import time

def read_file_to_memory(path):
    with open(path) as f:
        content = sorted([int(line.rstrip())for line in f])
        content.append(content[len(content)-1] + 3)
    return content


def main():
    start_time = time.time()
    all_data = read_file_to_memory('aoc10input.txt')   

    one_jolt_count = 0
    three_jolt_count = 0
    prev_adapter = 0
    for adapter in all_data:
        if adapter - prev_adapter == 1:
            one_jolt_count += 1
        else: 
            three_jolt_count += 1
        prev_adapter = adapter

    print(f'Answer: {one_jolt_count * three_jolt_count}')
    print(f'Took {time.time()-start_time} to run')


if __name__ == "__main__":
    main()
