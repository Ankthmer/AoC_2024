def part1(filename: str) -> int:

    with open(filename) as f:
        garden = [[[i, True] for i in line.strip()] for line in f]

    price = 0

    #Search in the garden
    for r, row in enumerate(garden):
        for c, col in enumerate(row):
            #If you find a letter that has not been visited yet, this is a new region
            if col[1] == True:
                #dim[0] represents the area and dim[1] represents the perimeter of the region
                dim = [0,0]
                #Calculate the area and the perimeter of the region
                dfs_part1(r, c, col[0], garden, dim)
                #Update the fence price
                price += dim[0]*dim[1]

    return price

def part2(filename: str) -> int:
    with open(filename) as f:
        garden = [[[i, True] for i in line.strip()] for line in f]

    price = 0

    #Search in the garden
    for r, row in enumerate(garden):
        for c, col in enumerate(row):
            #If you find a letter that has not been visited yet, this is a new region
            if col[1] == True:
                #dim[0] represents the area and dim[1] represents the number of sides of the region
                dim = [0,0]
                #edges[(0,1)] represents all lower edges, edges[(1,0)] represents all right edges, edges[(0,-1)] represents all upper edges and edges[(-1,0)] represents all left edges
                edges: dict[tuple[int, int], list[tuple[int, int]]] = {k: [] for k in {(0,1),(1,0),(0,-1),(-1,0)}}
                #Calculate the area and find all the edges of your region
                dfs_part2(r, c, col[0], garden, dim, edges)
                #Calculate the total number of sides
                get_sides(dim, edges)
                #Update the fence price
                price += dim[0]*dim[1]

    return price

def dfs_part1(r: int, c: int, flower: str, m: list[list[list[str, bool]]], dim: list[int, int]):

    #Represents all possible directions
    d = {(0,1),(1,0),(0,-1),(-1,0)}

    #Mark as visited
    m[r][c][1] = False
    #Increase the area by one
    dim[0] += 1

    #Move in every directions of one
    for (x,y) in d:
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x][0] != flower:
                raise IndexError

            #If you are still in the region and the next one has not been visited
            elif m[r+y][c+x][1] == True:
                #Visit it
                dfs_part1(r + y, c + x, flower, m, dim)

        #If you are outside the region increase the perimeter by one
        except IndexError:
            dim[1] += 1

    return

def dfs_part2(r: int, c: int, flower: str, m: list[list[list[str, bool]]], dim: list[int, int], edges: dict[tuple[int, int], list[tuple[int, int]]]):

    #Mark as visited
    m[r][c][1] = False
    #Increase the area by one
    dim[0] += 1

    #Move in every directions of one
    for (x,y) in edges.keys():
        try:
            if (r+y < 0) or (c+x < 0):
                raise IndexError

            if m[r+y][c+x][0] != flower:
                raise IndexError

            #If you are still in the region and the next one has not been visited
            elif m[r+y][c+x][1] == True:
                #Visit it
                dfs_part2(r + y, c + x, flower, m, dim, edges)

        #If you are outside the region add this point to the list of edges of the right type
        except IndexError:
            edges[(x,y)].append((r, c))

    return

def get_sides(dim: list[int, int], edges: dict[tuple[int, int], list[tuple[int, int]]]):

    for (x, y) in edges.keys():
        #For lower and upper edges
        if x == 0:
            d: dict[int, list[int]] = {}
            #For all the rows create a list of columns where there is an edge
            for (r, c) in edges[(x,y)]:
                if not r in d.keys():
                    d[r] = [c]
                else:
                    d[r].append(c)
        #For right and left edges
        else:
            d: dict[int, list[int]] = {}
            #For all the columns create a list of rows where there is an edge
            for (r, c) in edges[(x,y)]:
                if not c in d.keys():
                    d[c] = [r]
                else:
                    d[c].append(r)

        for i in d.keys():
            #Increase the number of sides by one
            dim[1] += 1
            d[i].sort()
            for j, el in enumerate(d[i]):
                try:
                    #Every time your list is not increasing by one increase the number of sides by one
                    if d[i][j+1] != el + 1:
                        dim[1] += 1
                except IndexError:
                    pass

    return

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
