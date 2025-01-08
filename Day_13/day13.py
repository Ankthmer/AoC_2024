import numpy as np
import re


class Machine:
    def __init__(self, a: np.ndarray, b: np.ndarray, prize: np.ndarray):
        self.a = a
        self.b = b
        self.prize = prize

def part1(filename: str) -> int:
    inp = get_input(filename)
    tokens = 0

    #For every machine solve the associeted linear system checking that the solution are positive integers
    for machine in inp:
        matrix = np.array([machine.a, machine.b, machine.prize])
        matrix[:, 1] = matrix[0,0]*matrix[:,1] - matrix[0,1]*matrix[:, 0]
        if (matrix[2,1] % matrix[1,1] == 0) and (matrix[1,1]*matrix[2,1] >= 0):
            y = matrix[2,1] // matrix[1,1]
            i = matrix[2,0] - matrix[1,0]*y
            if y <= 100 and (i % matrix[0,0] == 0) and (i*matrix[0,0] >= 0):
                x = i // matrix[0,0]
                if x <= 100:
                    tokens += x*3 + y

    return tokens

def part2(filename: str) -> int:
    inp = get_input(filename)
    tokens = 0

    #For every machine solve the associeted linear system verifying that the solutions are positive integers
    for machine in inp:
        matrix = np.array([machine.a, machine.b, machine.prize + 10000000000000])
        matrix[:, 1] = matrix[0,0]*matrix[:,1] - matrix[0,1]*matrix[:, 0]
        if (matrix[2,1] % matrix[1,1] == 0) and (matrix[1,1]*matrix[2,1] >= 0):
            y = matrix[2,1] // matrix[1,1]
            i = matrix[2,0] - matrix[1,0]*y
            if (i % matrix[0,0] == 0) and (i*matrix[0,0] >= 0):
                x = i // matrix[0,0]
                tokens += x*3 + y

    return tokens

def get_input(filename: str) -> list[Machine]:
    '''Parse the input remembering that every 4 lines the first is the button A, the second is the botton B and the third is the prize. Discard the fourth line.'''

    with open(filename) as f:
        machines: list[Machine] = []
        i = 0
        for line in f:
            if i == 0:
                a = np.array(list(map(int, re.findall("\d+", line))))
                i += 1
            elif i == 1:
                b = np.array(list(map(int, re.findall("\d+", line))))
                i += 1
            elif i == 2:
                prize = np.array(list(map(int, re.findall("\d+", line))))
                machines.append(Machine(a, b, prize))
                i += 1
            else:
                i = 0

    return machines


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
