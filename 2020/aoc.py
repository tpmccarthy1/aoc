def read_file_to_memory(path):
    with open(path) as f:
        content = [list(line.rstrip()) for line in f]
    return content

def intersection(lst1, lst2): 
    """ Ges the intersection of two lists """
    return [char for char in lst1 if char in lst2]

def find_intersections_of_groups(groups):
    """ Iterates over groups array creating an intersection of their sets until empty list if found """
    common_chars = groups[0]
    for i in range(0, len(groups)):
        common_chars = intersection(common_chars, groups[i])

    return common_chars

def flatten_groups(groups):
    """ Finds unique characters in list """
    flattened_group = set([item for sublist in groups for item in sublist])
    return flattened_group

def create_groups(groups):
    temp_group = []
    result_groups =[]
    for g in groups:      
        if not g:
            result_groups.append(temp_group)
            temp_group = []
            continue
        temp_group.append(g)

    if temp_group:
        result_groups.append(temp_group)
    
    return result_groups

def main():
    groups = create_groups(read_file_to_memory('aoc6input.txt'))
    part_one_count = 0
    part_two_cout = 0
    for g in groups:
        part_one_count += len(flatten_groups(g))
        ## pt 2
        part_two_cout += len(find_intersections_of_groups(g))

    print('Part 1: ' + str(part_one_count))
    print('Part 2: ' + str(part_two_cout))

if __name__ == "__main__":
    main()
