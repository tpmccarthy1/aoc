import sys


def get_range(pt1, pt2):
    if pt1 > pt2:
        return range(pt1, pt2-1, -1)
    else:
        return range(pt1, pt2 + 1)

def build_line_horizontal(x1, x2, y1, points):
    for num in get_range(x1, x2):
        if (num,  y1) in points:
            points[(num,  y1)] += 1
        else:
            points[(num, y1)] = 1


def build_line_vertical(x1, y1, y2, points):
    for num in get_range(y1, y2):
        if (x1,  num) in points:
            points[(x1,  num)] += 1
        else:
            points[(x1, num)] = 1


def build_line_diagonal(x1, x2, y1, y2, points):
    if(x1 < x2 and y1 > y2):
        while(x1 <= x2 and y1 >= y2):
            if (x1,  y1) in points:
                points[(x1,  y1)] += 1
            else:
                points[(x1, y1)] = 1
            x1 += 1
            y1 -= 1
    elif(x1 > x2 and y1 < y2):
        while(x1 >= x2 and y1 <= y2):
            if (x1,  y1) in points:
                points[(x1,  y1)] += 1
            else:
                points[(x1, y1)] = 1
            x1 -= 1
            y1 += 1
    elif(x1 < x2 and y1 < y2):
        while(x1 <= x2 and y1 <= y2):
            if (x1,  y1) in points:
                points[(x1,  y1)] += 1
            else:
                points[(x1, y1)] = 1
            x1 += 1
            y1 += 1
    elif(x1 > x2 and y1 > y2):
        while(x1 >= x2 and y1 >= y2):
            if (x1,  y1) in points:
                points[(x1,  y1)] += 1
            else:
                points[(x1, y1)] = 1
            x1 -= 1
            y1 -= 1


def main():
    points = {}

    with open(sys.argv[1]) as f:
        for line in f:
            line = list(line.strip().split('->'))

            x1 = int(line[0].split(',')[0])
            x2 = int(line[1].split(',')[0])
            y1 = int(line[0].split(',')[1])
            y2 = int(line[1].split(',')[1])

            # horizontal
            if (y1 == y2):
                build_line_horizontal(x1, x2, y1, points)

            # verticals
            elif (x1 == x2):
                build_line_vertical(x1, y1, y2, points)
            # diaganols
            else:
                build_line_diagonal(x1, x2, y1, y2, points)

    res = sum(value >= 2 for value in points.values())
    return res


if __name__ == "__main__":
    print(main())
