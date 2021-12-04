import sys

def play_bingo(input, boards):
    # iterate over inputs
    for b in input:
        # check all boards remove elements if found
        for board in boards:
            # try horizatontal
            for subboard in board:
                try:
                    i = subboard.index(b)
                    subboard[i] = -1
                    if all([n == -1 for n in subboard]):
                        return (b, board)
                except:
                    continue
            # check vertical
            for i in range(0, 5):
                for j in range(0, 5):
                    if board[j][i] > -1:
                        break
                    if board[j][i] == -1 and j == 4:
                        return(b, board)
                
    return (1, [])


def main():
    # get input and boards
    boards = []
    with open(sys.argv[1]) as f:
        # read first line
        input = list(map(int, f.readline().strip().split(',')))
        # read rest of lines
        while(True):
            line = f.readline()
            if not line:
                break
            if not line.strip():
                boards.append([])
                for r in range(0, 5):
                    nums = []
                    for num in f.readline().strip().split(' '):
                        if (num != ''):
                            nums.append(int(num.strip()))
                    boards[len(boards)-1].append(nums)
    
    (last_num, winner) = play_bingo(input, boards)
    total = 0
    for board in winner:
        for num in board:
            if num > 0:
                total += num 

    print(last_num * total)


if __name__ == "__main__":
    main()
