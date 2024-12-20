def part1(filename: str) -> int:

    with open(filename) as f:
        m = [[int(i) for i in line.strip()] for line in f]

    counter = 0

    for r,row in enumerate(m):
        for c, col in enumerate(row):
            if col == 0:
                counter += score_part1(m, r, c)
    return counter

def part2(filename: str) -> int:

    with open(filename) as f:
        m = [[int(i) for i in line.strip()] for line in f]

    counter = 0

    for r,row in enumerate(m):
        for c, col in enumerate(row):
            if col == 0:
                counter += score_part2(m, r, c)

    return counter

def score_part1(m: list[list[int]], r: int, c:int) -> int:
    fake = [[[i, True] for i in row] for row in m]

    path = []

    dfs_part1(path, fake, r, c)

    return path.count(9)

def dfs_part1(path: list[int], m: [list[list[int]]], r: int, c: int):

    d = {(0,1),(1,0),(0,-1),(-1,0)}

    m[r][c][1] = False

    for (x,y) in d:
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x][1] == True and m[r+y][c+x][0] == m[r][c][0] + 1:
                path.append(m[r+y][c+x][0])
                r = r+y
                c = c+x
                dfs_part1(path, m, r, c)
                r = r-y
                c = c-x

        except IndexError:
            pass
    return

def score_part2(m: list[list[int]], r: int, c:int) -> int:

    path = []

    dfs_part2(path, m, r, c)

    return path.count(9)

def dfs_part2(path: list[int], m: [list[list[int]]], r: int, c: int):

    d = {(0,1),(1,0),(0,-1),(-1,0)}

    for (x,y) in d:
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x] == m[r][c] + 1:
                path.append(m[r+y][c+x])
                r = r+y
                c = c+x
                dfs_part2(path, m, r, c)
                r = r-y
                c = c-x

        except IndexError:
            pass
    return


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
