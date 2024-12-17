def part1(filename: str) -> int:

    r, eq = get_input(filename)
    counter = 0

    for i, numbers in enumerate(eq):
        if try_op(r[i], numbers, len(numbers)-1) == True:
            counter += r[i]

    return counter

def part2(filename: str) -> int:
    r, eq = get_input(filename)
    counter = 0

    for i, numbers in enumerate(eq):
        if try_op_conc(r[i], numbers[0], numbers, 1) == True:
            counter += r[i]

    return counter

def get_input(filename: str) -> (list[int], list[list[int]]):

    with open(filename) as f:

        r = []
        eq = []

        for line in f:
            n, m = line.split(':')
            r.append(int(n))
            eq.append([int(i) for i in m.split()])

    return (r, eq)

def try_op(r: int, numbers: list[int], ind: int) -> bool:
    '''Ricorsive function'''
    if ind == 0:
        if r == numbers[ind]:
            return True
        else:
            return False

    elif r%numbers[ind] == 0:
        return (try_op(r/numbers[ind], numbers, ind-1) or try_op(r-numbers[ind], numbers, ind-1))
    else:
        return try_op(r-numbers[ind], numbers, ind-1)

    return False

def try_op_conc(r: int, par: int, numbers: list[int], ind: int) -> bool:
    '''Ricorsive function'''

    if ind == len(numbers):
        if r == par:
            return True
        else:
            return False

    elif par <= r:
        fake = conc(par, numbers, ind)
        return (try_op_conc(r, par*numbers[ind], numbers, ind+1) or
                try_op_conc(r, par+numbers[ind], numbers, ind+1) or
                try_op_conc(r, fake[0], fake, 1))

    else:
        return False

    return False

def conc(par: int, numbers: list[int], ind: int) -> list[int]:
    fake = []
    for i, num in enumerate(numbers):
        if i > ind:
            fake.append(num)
        elif i == ind:
            x = par*pow(10,len(str(num)))+num
            fake.append(x)

    return fake


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
