def read_file_to_memory(path):
    with open(path) as f:
        content = [line.rstrip().split(' ') for line in f]
    return content

def build_instructions_lst(lst):
    instructions = [[line[0], int(line[1]), False] for line in lst]
    return instructions

def run_instructions(instructions):
    acc = 0
    i = 0
    while (not instructions[i][2]):
        instruction = instructions[i]      
        instruction[2] = True
        if instruction[0] == 'acc':
            acc+=instruction[1]
            i+=1
        elif instruction[0] == 'nop':
            i+=1
        else:
            i += instruction[1] 
    return acc

def main():
    # Read the file into memory for proccessing
    file_content = read_file_to_memory('aoc8input.txt')
    instructions = build_instructions_lst(file_content)
    acc = run_instructions(instructions)
    
    print(acc)



if __name__ == "__main__":
    main()
