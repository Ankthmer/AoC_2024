from functools import cmp_to_key
from typing import Callable

def part1(filename: str) -> int:

    d, updates = get_input(filename)
    counter = 0

    for up in updates:
        #If the update is correct increase de counter.
        if check_up(up, d) == True:
            counter += up[int(len(up)/2)]

    return counter


def part2(filename: str) -> int:
    d, updates = get_input(filename)
    counter = 0

    for up in updates:
        #If the update is incorrect reorder the pages and increase the counter.
        if check_up(up, d) == False:
            up.sort(key = cmp_to_key(make_cmp(d)))
            counter += up[int(len(up)/2)]

    return counter

def get_input(filename: str) -> tuple[dict[int, set[int]] , list[list[int]]]:
    """Take the input from the file."""

    with open(filename) as f:
        it = iter(f)
        d: dict[int, set[int]] = {}

        #First create a dictionary with the ordering rules, where every keys is a number and refers to the set of its subsequent numbers.
        for line in it:
            #If you find a blank line it means that you have collected all the ordering rules.
            if line == '\n':
                break
            else:
                k, p = map(int, line.split('|'))
                if not k in d.keys():
                    d[int(k)]= {int(p)}
                else:
                    d[int(k)].add(int(p))

        #Then create a list with all the updates.
        updates = [list(map(int,line.split(','))) for line in it]

    return (d, updates)

def check_up(up: list[int], d: dict[int, set[int]]) -> bool:
    """Check that the pages of an update are in the correct order (according to the ordering rules)."""
    check = True

    for i, u in enumerate(up):
        for j, test in enumerate(up):
            try:
                #If a number is before one of its previous numbers (according to the ordering rules), the update is not correct.
                if j > i and (u in d[test]):
                    check = False
                    break
            except KeyError:
                pass

    return check


def comp(n1: int, n2: int, d: dict[int, set[int]]) -> int:
    """Take two number and compare them according to the ordering rules."""
    if n1 == n2:
        return 0
    try:
        if n1 in d[n2]:
            return 1
    except KeyError:
        pass
    try:
        if n2 in d[n1]:
            return -1
    except KeyError:
        pass
    assert False


def make_cmp(d: dict[int, set[int]]) -> Callable[[int, int], int]:
    """Create a comparator that can be used with the built-in sort function."""
    def wrapper(n1: int, n2: int):
        return comp(n1, n2, d)

    return wrapper


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
