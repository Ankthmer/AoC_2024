def part1(filename: str) -> int:
    reports = get_input(filename)

    counter = 0

    for rep in reports:

        #If the numbers are not increasing, reverse the numbers in the report
        if rep[0] > rep[1]:
            rep.reverse()

        #If the numbers in the report are all increasing not too fast the report is safe
        if all(rep[i+1]-rep[i] in range(1,4) for i in range(0, len(rep)-1)):
            counter += 1

    return counter

def part2(filename: str) -> int:
    reports = get_input(filename)

    counter = 0

    for rep in reports:

        #Search if the numbers in the report are generally increasing (or generally decreasing) not too fast
        check1 = [rep[i+1]-rep[i] in range(1,4) for i in range (0,len(rep)-1)]
        check2 = [rep[i]-rep[i+1] in range(1,4) for i in range (0,len(rep)-1)]

        v1 = check1.count(True)
        v2 = check2.count(True)


        #If the numbers in the report are all increasing (or all decreasing) not too fast the report is safe
        if all(check1) or all(check2):
            counter += 1
        else:
            #If they are generally decreasing reverse the numbers in the report in order to reduce to the generally increasing case
            if v2 > v1:
                rep.reverse()

            for j, el in enumerate(rep):
                #Suppress one of your elements
                t = [rep[i] for i in range(0,len(rep)) if i != j]

                #If one of the combinations works the report is safe and you don't need to check the others
                if all(t[i+1]-t[i] in range(1,4) for i in range(0, len(t)-1)):
                    counter += 1
                    break

    return counter

def get_input(filename: str) -> list[list[int]]:
    with open(filename) as f:
        lines = [[int(x) for x in line.split()] for line in f]

    return lines

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
