def part1(filename: str) -> int:
    with open(filename) as f:
        m = [[i for i in line.strip()] for line in f]

    r, c = get_pos(m, '^')

    return count_pos(m, r, c, '#')



def part2(filename: str) -> int:
    with open(filename) as f:
        m = [[i for i in line.strip()] for line in f]

    r, c = get_pos(m, '^')
    counter = 0

    mod = [line.copy() for line in m]

    count_pos(mod, r, c, '#')

    for i, row in enumerate(mod):
        for j, char in enumerate(row):
            if char == 'X' and (i != r or j != c):
                cop = [line.copy() for line in m]
                cop[i][j] = '#'
                if count_pos(cop, r, c, '#') == 0:
                    counter += 1

    return counter

def get_pos(m: list[list[str]], s: str) -> (int, int):
    '''Return row and column indexes of the first occurence of a specific substring'''
    for i, line in enumerate(m):
        if m[i].count(s)>0:
            r = i
            c = m[i].index(s)
            break
    return (r, c)

def count_pos(m: list[list[str]], r: int, c: int, s: str):
    '''Count how many positions the guard will visit, if there is a cycle return 0'''
    x = 0
    y = -1
    end = False
    counter = 1
    mark = 'X'
    m[r][c] = mark
    arrivals = []


    #If the guard is not at the border of the map
    if r+y in range(0, len(m)) and c+x in range(0, len(m[0])):

        #While the guard is still on the map
        while end == False:
            try:
                #The guard goes forward until the guard founds a marker
                while (m[r+y][c+x] != s):
                    if r+y < 0 or c+x < 0:
                        raise IndexError
                    if m[r+y][c+x] != mark:
                        m[r+y][c+x] = mark
                        counter += 1

                    r += y
                    c += x

                if arrivals.count((r,c)) > 1:
                    return 0
                arrivals.append((r,c))
                #Then the guard turns right
                if (x,y) == (0,-1):
                    (x,y) = (1,0)
                elif (x,y) == (1,0):
                    (x,y) = (0,1)
                elif (x,y) == (0,1):
                    (x,y) = (-1,0)
                else:
                    (x,y) = (0,-1)

            except IndexError:
                end = True

    return counter

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
