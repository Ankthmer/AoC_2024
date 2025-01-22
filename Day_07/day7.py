def part1(filename: str) -> int:

    r, eq = get_input(filename)
    counter = 0

    for i, numbers in enumerate(eq):
        #If there is a way to obtain an identity between the test value and the other numbers, update the counter.
        if try_op(r[i], numbers, len(numbers)-1) == True:
            counter += r[i]

    return counter

def part2(filename: str) -> int:
    r, eq = get_input(filename)
    counter = 0

    for i, numbers in enumerate(eq):
        #If there is a way to obtain an identity between the test value and the other numbers, update the counter.
        if try_op_conc(r[i], numbers[0], numbers, 1) == True:
            counter += r[i]

    return counter

def get_input(filename: str) -> (list[int], list[list[int]]):
    """Take the input from the file."""

    with open(filename) as f:

        #Represent the test numbers.
        r = []
        #Represent the lists of numbers associated with the related test numbers.
        eq = []

        for line in f:
            n, m = line.split(':')
            r.append(int(n))
            eq.append([int(i) for i in m.split()])

    return (r, eq)

def try_op(r: int, numbers: list[int], ind: int) -> bool:
    '''Ricorsive function. Check if there is a way to obtain an identity between the value of r and the other numbers.'''

    #If this is the last numbe check if it is equal to the test value.
    if ind == 0:
        if r == numbers[ind]:
            return True
        else:
            return False

    #Otherwise if r is divisible for the number at index ind:
    elif r%numbers[ind] == 0:
        #Try dividing or subtracting r for the number at index ind.
        return (try_op(r/numbers[ind], numbers, ind-1) or try_op(r-numbers[ind], numbers, ind-1))
    else:
        #Otherwise try subtracting r for the number at index ind.
        return try_op(r-numbers[ind], numbers, ind-1)

    return False

def try_op_conc(r: int, par: int, numbers: list[int], ind: int) -> bool:
    '''Ricorsive function. Check if there is a way to obtain an identity between the value of r and the other numbers adding the rule of concatenation. "par" represents the current value of your operation.'''

    #If this is the last numbe check if it is equal to the test value.
    if ind == len(numbers):
        if r == par:
            return True
        else:
            return False

    #Otherwise if the current value is less then r:
    elif par <= r:
        #Make a copy of the remaining numbers in your list and put as first number the current value of par concatenated with de first number.
        fake = conc(par, numbers, ind)

        #Try adding or multiply par for the number at index ind and try to see if fake works.
        return (try_op_conc(r, par*numbers[ind], numbers, ind+1) or
                try_op_conc(r, par+numbers[ind], numbers, ind+1) or
                try_op_conc(r, fake[0], fake, 1))

    else:
        return False

    return False

def conc(par: int, numbers: list[int], ind: int) -> list[int]:
    '''Make a list of integer using "par" concatenated with the number at index "ind" as first number and then copy the rest of list.'''
    fake = []
    for i, num in enumerate(numbers):
        if i > ind:
            fake.append(num)
        elif i == ind:
            #Concatenate the current value with the number at index ind.
            x = par*pow(10,len(str(num)))+num
            fake.append(x)

    return fake


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
