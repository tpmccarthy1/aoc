import time

def read_file_to_memory(path):
    with open(path) as f:
        content = sorted([int(line.rstrip())for line in f])
        content.append(content[len(content)-1] + 3)
    return content

def count_permutations(lst):
    """ Takes a list of 4 numbers and counts the number of valid permuations """
    # Base case
    if len(lst) == 1:
        return 0
    # First position counts as 1 permutaion
    count = 0
    num_to_test = lst[0] 
    for num in lst[:4]:
        if num != num_to_test and num - num_to_test <= 3:
            count += 1
    # remove num_to_test from lst
    lst.pop(0)

    # return the count minus 1 to account for the original permuation
    return count + count_permutations(lst)


def main():
    start_time = time.time()
    all_data = read_file_to_memory('aoc10input.txt')   
    all_permutations = count_permutations(all_data)  
    print(f'Took {time.time()-start_time} to run')


if __name__ == "__main__":
    main()
