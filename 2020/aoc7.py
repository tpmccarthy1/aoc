import re

def read_file_to_memory(path):
    with open(path) as f:
        content = [line.rstrip() for line in f]
    return content

# Filter shiny type bags
def holds_shiny_bag(s): 
    return 'shiny gold' in s and not s.startswith('shiny gold')

# Map line to single outer bag type
def get_outer_bag_types(s): 
    bag_string = s.split('bags')[0]
    ## Get bag type before words bags
    return bag_string[:len(bag_string)].strip()

def build_bag_capacity_dict(bag_data):
    bag_dict = {}
    for line in bag_data:
        bag_string = line.split('bags')[0].strip()
        if not bag_string in bag_dict:
            inner_bags = re.split(r'(\d+)', line)
            arr = []
            for i in range(0, len(inner_bags)):
                if inner_bags[i].isnumeric():
                    arr.append([int(inner_bags[i]), 
                    ' '.join(s for s in inner_bags[i+1].split(' ') if 'bag' not in s and 'bags' not in s).strip(' ')])
            bag_dict[bag_string] = arr
    return bag_dict



def make_bag_map(bag_dict, outer_bag_types):
    def count_shiny_golds(s):
        count = 0
        for bag in outer_bag_types:
            if bag in s:
                start_index = int(s.index(bag)-2)
                if (start_index > 0):
                    count += int(s[start_index])
                else:
                    count += 1
        return count
    return count_shiny_golds

def main():
    file_content = read_file_to_memory('aoc7input.txt')
    ## bag types that contain shiny bag directly
    outer_bag_types = list(map(get_outer_bag_types, filter(holds_shiny_bag, file_content)))
    ## get list of lines that have bag type in base_shiny_bag_holders
    bag_dict = build_bag_capacity_dict(file_content)
    
    shiny_gold_map = make_bag_map(bag_dict, outer_bag_types)
    total_bags = list(map(shiny_gold_map, file_content))
    print('0')

if __name__ == "__main__":
    main()