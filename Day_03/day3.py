def part1(filename: str) -> int:

    #Take your input.
    with open(filename) as f:
        p = "".join(line.strip() for line in f)

    return occurrences(p)

def part2(filename: str) -> int:

    #Take your input.
    with open(filename) as f:
        p = "".join(line.strip() for line in f)

    return occ_on_off(p)


def occurrences(p: str) -> int:

    counter = 0

    for i in range(7, len(p)):
        try:
            #If you find ')' and you find that the previous one is a number go backwar:
            if p[i] == ')' and p[i-1].isnumeric():
                for j in range(i-1, -1, -1):
                    if p[j].isnumeric():
                        pass
                    #if after some numbers you find ',' and that the previous one is a number save the number between ',' and ')'. Then go backward:
                    elif p[j] == ',' and p[j-1].isnumeric():
                            a = int(p[j+1:i])
                            for m in range(j-1, -1, -1):
                                if p[m].isnumeric():
                                    pass
                                #if after some numbers you find 'mul(' save the number between '(' and ',' and update your counter.
                                elif p[m-3 : m+1] == 'mul(':
                                    b = int(p[m+1:j])
                                    counter += a*b
                                    break
                                else:
                                    break
                    else:
                        break
        except IndexError:
            pass

    return counter

def occ_on_off(p: str) -> int:

    counter = 0
    click = 'do()'

    for i in range(7, len(p)):
        try:
            if p[i-3:i+1] == 'do()':
                click = 'do()'
            elif p[i-6:i+1] == "don't()":
                click = "don't()"

            #If you find ')' and you find that the previous one is a number and click equals do() go backward:
            elif p[i] == ')' and p[i-1].isdigit() and click == 'do()':
                for j in range(i-1, -1, -1):
                    if p[j].isnumeric():
                        pass
                    #if after some numbers you find ',' and that the previous one is a number save the number between ',' and ')'. Then go backward:
                    elif p[j] == ',' and p[j-1].isnumeric():
                            a = int(p[j+1:i])

                            for m in range(j-1, -1, -1):
                                if p[m].isnumeric():
                                    pass
                                #if after some numbers you find 'mul(' save the number between '(' and ',' and update your counter.
                                elif p[m-3 : m+1] == 'mul(':
                                    b = int(p[m+1:j])

                                    counter += a*b
                                    break
                                else:
                                    break
                    else:
                        break
        except IndexError:
            pass

    return counter

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.5.txt'))
    print(part2('input2.txt'))
