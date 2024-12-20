def part1(filename: str) -> int:
    with open(filename) as f:
        inp = f.readline()

    #Create the sequence
    seq = create(inp)

    sort_seq(seq)

    return sum(seq[i]*i for i in range(0,len(seq)) if seq[i] != -1)

def part2(filename: str) -> int:

    with open(filename) as f:
        inp = f.readline()

    seq = create_part2(inp)

    return sum(seq[i]*i for i in range(0,len(seq)) if seq[i] != -1)

def create(inp: str) -> list[int]:

    seq = []
    if len(inp)%2 == 1:
        inp += '0'

    for i in range(0, len(inp), 2):
        seq += [i//2] * int(inp[i]) + [-1] * int(inp[i+1])

    return seq

def sort_seq(seq: list[int]):

    j = len(seq) - 1

    for i, num in enumerate(seq):
        if num == -1:
            while seq[j] == -1:
                j -= 1

            if i >= j:
                break

            seq[i] = seq[j]
            seq[j] = -1

    return

def create_part2(inp: str) -> list[int]:

    spaces = [int(inp[i]) for i in range(0, len(inp)) if i%2 == 1]
    spaces += [0]
    files = [int(inp[i]) for i in range(0, len(inp)) if i%2 == 0]
    seq = []
    used: dict[int, int] = {}

    for i in range(0, len(files)):
        if files[i] != -1:
            seq += [i] * files[i]
            files[i] = -1
        else:
            seq += [-1] * used[i]

        for j in range(len(files) - 1, i, -1):
            if -1 < files[j] <= spaces[i]:
                seq += [j] * files[j]
                spaces[i] -= files[j]
                used[j] = files[j]
                files[j] = -1
            if spaces[i] <= 0:
                break

        if spaces[i] > 0:
            seq += [-1] * spaces[i]

    return seq




if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
