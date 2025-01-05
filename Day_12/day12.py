def part1(filename: str) -> int:

    with open(filename) as f:
        garden = [[[i, True] for i in line.strip()] for line in f]

    return total(garden)

def part2(filename: str) -> int:
    with open(filename) as f:
        garden = [[[i, True] for i in line.strip()] for line in f]

    return discount(garden)

def total(garden: list[list[list[str, bool]]]) -> int:

    price = 0

    for r, row in enumerate(garden):
        for c, col in enumerate(row):
            if col[1] == True:
                dim = [0,0]
                dfs_part1(r, c, col[0], garden, dim)
                price += dim[0]*dim[1]

    return price

def discount(garden: list[list[list[str, bool]]]) -> int:

    price = 0

    for r, row in enumerate(garden):
        for c, col in enumerate(row):
            if col[1] == True:
                #The area is 0 and you have 1 side
                dim = [0,0]
                edges = {k: [] for k in {(0,1),(1,0),(0,-1),(-1,0)}}
                dfs_part2(r, c, col[0], garden, dim, edges)
                get_sides(dim, edges)
                price += dim[0]*dim[1]

    return price

def dfs_part1(r: int, c: int, flower: str, m: list[list[list[str, bool]]], dim: list[int, int]):

    d = {(0,1),(1,0),(0,-1),(-1,0)}

    m[r][c][1] = False
    dim[0] += 1

    for (x,y) in d:
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x][0] != flower:
                raise IndexError

            elif m[r+y][c+x][1] == True:
                dfs_part1(r + y, c + x, flower, m, dim)

        except IndexError:
            dim[1] += 1

    return

def dfs_part2_old(r: int, c: int, flower: str, m: list[list[list[str, bool]]], dim: list[int, int], rp, cp):

    #Possible directions
    d = {(-1,0),(0,-1),(1,0),(0,1)}

    #Increase the area
    dim[0] += 1
    #Mark as visited
    m[r][c][1] = False

    #If this is the first one
    if r == rp and c == cp:
        counter = 0
        #Count the number of directions in which you find an edge
        for (x,y) in d:
            try:
                if m[r+y][c+x][0] != flower or r+y < 0 or c+x < 0:
                    raise IndexError
            except IndexError:
                counter += 1
        if counter == 3:
            dim[1] += 2
        elif counter == 4:
            dim[1] += 3

    #For every direction
    for (x,y) in d:
        try:
            #If you are near the edge of the garden
            if (r+y < 0) or (c+x < 0):
                #See if this is a new side
                raise IndexError

            #Or near the edge of the region
            if m[r+y][c+x][0] != flower:
                #See if this is a new side
                raise IndexError

            #If you are still in the region and the next one (in that direction) is not visited
            elif m[r+y][c+x][1] == True:
                dfs_part2(r + y, c + x, flower, m, dim, r, c)

        except IndexError:
            try:
                #If the previus one in this direction was also on the edge of the region
                if m[rp + y][cp + x][0] != flower or rp + y < 0 or cp + x < 0:
                    #Do nothing beacause you have already counted this side
                    raise IndexError
                else:
                    #Increase the number of sides by 1
                    dim[1] += 1
            except IndexError:
                pass


    return

def dfs_part2(r: int, c: int, flower: str, m: list[list[list[str, bool]]], dim: list[int, int], edges: dict[(int, int), list[(int, int)]]):

    m[r][c][1] = False
    dim[0] += 1

    for (x,y) in edges.keys():
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x][0] != flower:
                raise IndexError

            elif m[r+y][c+x][1] == True:
                dfs_part2(r + y, c + x, flower, m, dim, edges)

        except IndexError:
            edges[(x,y)].append((r, c))

    return

def get_sides(dim: list[int, int], edges: dict[(int, int), list[(int, int)]]):

    for (x, y) in edges.keys():
        if x == 0:
            d: dict[int, list[int]] = {}
            for (r, c) in edges[(x,y)]:
                if not r in d.keys():
                    d[r] = [c]
                else:
                    d[r].append(c)
        else:
            d: dict[int, list[int]] = {}
            for (r, c) in edges[(x,y)]:
                if not c in d.keys():
                    d[c] = [r]
                else:
                    d[c].append(r)

        for i in d.keys():
            dim[1] += 1
            d[i].sort()
            for j, el in enumerate(d[i]):
                try:
                    if d[i][j+1] != el + 1:
                        dim[1] += 1
                except IndexError:
                    pass




if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
