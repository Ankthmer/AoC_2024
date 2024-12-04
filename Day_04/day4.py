def part1(puzzle_filename: str) -> int:

    counter = 0

    #Read the file and produce a list of str
    with open(puzzle_filename) as f:
        lines = [line for line in f]

    #Find the total number of occurrences
    for x, row in enumerate(lines):
        for y, char in enumerate(row):

            #Search the Xs in your matrix
            if char == 'X':

                #Search XMAS in every direction
                for dx, dy in [(dx,dy)
                               for dx in range(-1,2)
                               for dy in range(-1,2)
                               if (dx,dy) != (0,0)
                               ]:
                    try:
                        if (x+3*dx > -1 and y+3*dy > -1
                            and lines[x+dx][y+dy] == 'M' and lines[x+2*dx][y+2*dy] == 'A' and lines[x+3*dx][y+3*dy] == 'S'
                            ):
                            counter += 1
                    except IndexError:
                        pass

    return counter

def part2(puzzle_filename: str) -> int:

    counter = 0
    mas = set('MS')

    #Read the file and produce a list of str
    with open(puzzle_filename) as f:
        lines = [line for line in f]

    #Find the total number of occurrences
    for x, row in enumerate(lines):
        for y, char in enumerate(row):

            #Search the As in your matrix
            if char == 'A':

                try:
                    if (x-1 > -1 and y-1 > -1
                        #Check the first diagonal
                        and {lines[x-1][y-1], lines [x+1][y+1]} == mas
                        #Check the second diagonal
                        and {lines[x-1][y+1], lines [x+1][y-1]} == mas
                        ) :
                        counter += 1
                except IndexError:
                    pass

    return counter

if __name__ == "__main__":
    print(part1('puzzle1.txt'))
    print(part1('puzzle2.txt'))
    print(part2('puzzle1.txt'))
    print(part2('puzzle2.txt'))
