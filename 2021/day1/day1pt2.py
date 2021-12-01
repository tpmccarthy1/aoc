def read_file_to_memory(path):
    with open(path) as f:
        content = [int(line) for line in f]
    return content



def main():
    content = read_file_to_memory('input.txt')

    window_sum = [sum(content[0 : 0+3])]
    i = 1
    increases = 0
    for line in content[1:]:
        temp = [sum(content[i : i+3])]
        if temp > window_sum:
            increases+=1
        window_sum = temp
        i+=1
    
    print(increases)





if __name__ == "__main__":
    main()
