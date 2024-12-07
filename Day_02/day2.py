def part1(filename: str) -> int:
    reports = get_input(filename)

    counter = 0

    return sum(check(rep) == True for rep in reports)

def part2(filename: str) -> int:
    reports = get_input(filename)

    counter = 0

    for rep in reports:

        if check(rep) == True:
            counter += 1
        else:
            for j, el in enumerate(rep):
                #Suppress one of your elements
                t = [rep[i] for i in range(0,len(rep)) if i != j]

                #If one of the combinations works the report is safe and you don't need to check the others
                if check(t) == True:
                    counter += 1
                    break

    return counter

def get_input(filename: str) -> list[list[int]]:
    with open(filename) as f:
        lines = [[int(x) for x in line.split()] for line in f]

    return lines

def check(rep: list[int]) -> bool:
    '''If the numbers in the report are all increasing (or all decreasing) not too fast the report is safe'''
    if (all(rep[i+1]-rep[i] in range(1,4) for i in range (0,len(rep)-1)) or
        all(rep[i]-rep[i+1] in range(1,4) for i in range (0,len(rep)-1))
        ):
        return True
    else:
        return False




if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
