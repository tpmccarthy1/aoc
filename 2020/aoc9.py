import time

def read_file_to_memory(path):
    with open(path) as f:
        content = [int(line.rstrip())for line in f]
    return content

def get_preamble(all_data, start_index, len):
    return all_data[start_index:start_index+len]

def map_sums(start, preamble, length):
    sums = []
    first = preamble[start]
    for i in range(1, length):
        sums.append(first + preamble[i])
    return sums

def check_sum(target, preamble, length):
    i = 0
    while(i < length):
        sums_to_try = map_sums(i, preamble, length)
        if not target in sums_to_try:
            i+=1
        else:
            return True
    return False

def main():
    start_time = time.time()
    all_data = read_file_to_memory('aoc9input.txt')   
    preamble_length = 25
    all_data_length = len(all_data)
    start_index = 0
    preamble = get_preamble(all_data, start_index, preamble_length)
    non_sum_number = None

    ## pt 1
    for i in range(start_index+preamble_length, all_data_length):
        if not check_sum(all_data[i], preamble, preamble_length):
            non_sum_number = all_data[i]
            index_of_invalid_num = i
            break
        start_index += 1
        preamble = get_preamble(all_data, start_index, preamble_length)

    print(f'Pt 1: {non_sum_number}')

    ## pt 2
    nums = []
    start = 0
    end = 1
    while not sum(nums) == non_sum_number:
        nums = all_data[start:end]
        if (sum(nums) > non_sum_number):
            start += 1
            end = start + 1
        else:
           end += 1

    print(f'Pt 2: {min(nums) + max(nums)}')
    print(f'Took {time.time()-start_time} to run')


if __name__ == "__main__":
    main()
