from functools import wraps

def part1(filename: str) -> int:

    with open(filename) as f:
        stones = f.readline().split()

    counter = 0

    for stone in stones:
        counter += blink(stone, 25)

    return counter

def part2(filename: str) -> int:

    with open(filename) as f:
        stones = f.readline().split()

    counter = 0

    for stone in stones:
        counter += blink(stone, 75)

    return counter

def memoize(func):
    chace = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in chace:
            chace[key] = func(*args, **kwargs)

        return chace[key]

    return wrapper

@memoize
def blink(stone: str, times: int) -> int:

    if times == 0:
        return 1

    else:
        if stone == '0':
            return blink('1', times - 1)
        elif len(stone)%2 == 0:
            return (blink(stone[0:len(stone)//2], times - 1)
                    + blink(str(int(stone[len(stone)//2:len(stone)])), times - 1))
        else:
            return blink(str(int(stone)*2024), times - 1)


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))




