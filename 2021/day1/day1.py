def read_file_to_memory(path):
    with open(path) as f:
        content = [int(line) for line in f]
    return content



def main():
    content = read_file_to_memory('input.txt')
    
    increases = 0
    prev = 0

    for line in content[1:]: 
        if line > prev:
            increases += 1
        prev = line

    print(increases)


if __name__ == "__main__":
    main()
