def parse_commands(path):
    with open(path) as f:
        x = 0
        y = 0
        for line in f:
            parts = line.split()
            if(parts[0] == ('down')):
                y += int(parts[1])
            elif(parts[0] == ('up')):
                y -= int(parts[1])
            elif(parts[0] == ('forward')):
                x += int(parts[1])
            else:
                x -= int(parts[1])
    return (x, y)



def main():
    coords = parse_commands("input.txt")

    print(coords[0] * coords[1])

if __name__ == "__main__":
    main()
