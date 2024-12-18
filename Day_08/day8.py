from itertools import product

def part1(filename: str) -> int:
    with open(filename) as f:
        inp = [line.strip() for line in f]

    n = len(inp)
    m = len(inp[0])

    d = get_indexes(inp)

    return len(get_nodes(d,n,m))

def part2(filename: str) -> int:
    with open(filename) as f:
        inp = [line.strip() for line in f]

    n = len(inp)
    m = len(inp[0])

    d = get_indexes(inp)

    return len(get_nodes_part2(d,n,m))

def get_indexes(inp: list[str]) -> dict[str, set[tuple[int, int]]]:
    d: dict[str, set[tuple[int, int]]] = {}

    for y , line in enumerate(inp):
        for x, col in enumerate(line):
            if col != '.':
                if col in d.keys():
                    d[col].add((x, y))
                else:
                    d[col] = {(x, y)}
    return d

def get_nodes(d: dict[str, set[tuple[int, int]]], n: int, m: int) -> set[tuple[int, int]]:
    nodes: set[tuple[int, int]] = set()

    for s in d.values():
        for ant1, ant2 in product(s, repeat = 2):
            if ant1 >= ant2:
                continue
            x1, y1 = ant1
            x2, y2 = ant2

            assert x1 <= x2

            dx = x2 - x1
            dy = y2 - y1

            if (-1 < x1 - dx < m) and (-1 < y1 - dy < n):
                    nodes.add((x1 - dx, y1 - dy))
            if (-1 < x2 + dx < m) and (-1 < y2 + dy < n):
                    nodes.add((x2 + dx, y2 + dy))

    return nodes

def get_nodes_part2(d: dict[str, set[tuple[int, int]]], n: int, m: int) -> set[tuple[int, int]]:
    nodes: set[tuple[int, int]] = set()

    for s in d.values():
        for ant1, ant2 in product(s, repeat = 2):
            if ant1 >= ant2:
                continue
            nodes.add(ant1)
            nodes.add(ant2)
            x1, y1 = ant1
            x2, y2 = ant2

            assert x1 <= x2

            dx = x2 - x1
            dy = y2 - y1

            while (-1 < x1 - dx < m) and (-1 < y1 - dy < n):
                nodes.add((x1 - dx, y1 - dy))
                x1 -= dx
                y1 -= dy
            while (-1 < x2 + dx < m) and (-1 < y2 + dy < n):
                nodes.add((x2 + dx, y2 + dy))
                x2 += dx
                y2 += dy

    return nodes

if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
