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
    index_of_last_jmp = None
    acc_since_last_jmp = 0
    done = False
    length = len(instructions)
    while (i < length and not instructions[i][2]):   
        instruction = instructions[i] 
        temp_increment = instruction[1] if instruction[0] == 'jmp' else 1
        if instruction[0] != 'acc' and instructions[i + temp_increment][2]:
            instructions[index_of_last_jmp][0] = 'jmp' if instructions[index_of_last_jmp][0] == 'nop' else 'nop'
            ## mark all as unseen to not hit this condition
            for i in instructions:
                i[2] = False
            i = index_of_last_jmp
            done = True
            continue
        instruction[2] = True
        if instruction[0] == 'acc':
            acc += instruction[1]
            acc_since_last_jmp += instruction[1]
            i+=1
        elif instruction[0] == 'nop':
            if not done:
                acc_since_last_jmp =0
            index_of_last_jmp = i
            i+=1
        elif instruction[0] == 'jmp':
            if not done: 
                acc_since_last_jmp =0
            index_of_last_jmp = i
            i += instruction[1] 

    return acc - acc_since_last_jmp

def main():
    file_content = read_file_to_memory('aoc8input.txt')
    instructions = build_instructions_lst(file_content)
    acc = run_instructions(instructions)
    
    print(acc)

if __name__ == "__main__":
    main()
