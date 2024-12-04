def part1(filename: str) -> int:

    list1, list2 = map(sorted, get_input(filename))

    return sum(abs(b-a) for a,b in zip(list1,list2))

def part2(filename: str) -> int:

    columns = get_input(filename)

    def create_dict(l: list) -> dict :
        d: dict[int, int] = {}
        for v in l:
            n = d.get(v,0)
            d[v] = n+1
        return d

    d1, d2 = map(create_dict, columns)

    return sum(v * d1[v] * d2[v] for v in d1 if v in d2)

def get_input(filename: str) -> tuple[list[int], list[int]]:
    '''Create two list of integers representing the columns of the file'''

    with open(filename) as f:
        list1, list2 = [], []

        for line in f:
            a, b = map(int, line.split())
            list1.append(a)
            list2.append(b)

    return list1, list2

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))





