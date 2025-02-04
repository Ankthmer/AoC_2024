def part1(filename: str) -> int:
    with open(filename) as f:
        inp = f.readline()

    #Generate a sequence of numbers based on the input data.
    seq = create(inp)

    #Fill the empty spaces by moving elements from the end of the sequence.
    sort_seq(seq)

    #Sum the results of multiplying each block's position by the file ID it contains.
    return sum(seq[i]*i for i in range(0,len(seq)) if seq[i] != -1)

def part2(filename: str) -> int:

    with open(filename) as f:
        inp = f.readline()

    #Generate a sequence of numbers based on the input data.
    seq = create_sorted(inp)

    return sum(seq[i]*i for i in range(0,len(seq)) if seq[i] != -1)

def create(inp: str) -> list[int]:
    '''Generate a sequence of numbers based on the input data.
    The digits of the input alternate between indicating the length of a file and the length of free space.
    '''

    seq = []

    #If the input has an odd number of digits, append a zero at the end.
    if len(inp)%2 == 1:
        inp += '0'

    #For every pair of numbers in the sequence:
    for i in range(0, len(inp), 2):

        #Add the file number to the sequence as many times as specified by the first number, followed by blank spaces (represented as -1) as indicated by the second number.
        seq += [i//2] * int(inp[i]) + [-1] * int(inp[i+1])

    return seq

def sort_seq(seq: list[int]):

    j = len(seq) - 1

    for i, num in enumerate(seq):
        #If there is a blank space:
        if num == -1:
            #Take the last number of the sequence.
            while seq[j] == -1:
                j -= 1

            #If the empty space is next to the last number in the sequence, stop the loop.
            if i >= j:
                break

            #Fill the empty space with the last number.
            seq[i] = seq[j]
            seq[j] = -1

    return

def create_sorted(inp: str) -> list[int]:
    '''
    Generate a sequence of numbers based on the input data.
    The digits alternate between representing file lengths and free space lengths.
    Instead of creating the sequence strictly according to this information, replace free spaces by moving whole files from the end of the input.
    '''

    #Store the numbers representing free spaces in a list.
    spaces = [int(inp[i]) for i in range(0, len(inp)) if i%2 == 1]
    #Append an extra zero at the end.
    spaces += [0]
    #Store the numbers representing files in an list.
    files = [int(inp[i]) for i in range(0, len(inp)) if i%2 == 0]
    seq = []
    #Create a dictionary where the already used numbers can be stored.
    used: dict[int, int] = {}

    for i in range(0, len(files)):
        #If the file is not already used:
        if files[i] != -1:
            #Add it to your sequence.
            seq += [i] * files[i]
            #Mark it as used.
            files[i] = -1
        else:
            #Otherwise, add the corresponding number of empty spaces.
            seq += [-1] * used[i]

        #Starting from the end of the list:
        for j in range(len(files) - 1, i, -1):
            #Find the first unused number that is less than or equal to the next number in the spaces list:
            if -1 < files[j] <= spaces[i]:
                #Add the corresponding number of files to your sequence.
                seq += [j] * files[j]
                #Update the number of empty spaces left.
                spaces[i] -= files[j]
                #Mark the number of the file as used.
                used[j] = files[j]
                files[j] = -1
            #If there are no more empty spaces left, break the loop.
            if spaces[i] <= 0:
                break
        #If there are any empty spaces left, add them to the sequence.
        if spaces[i] > 0:
            seq += [-1] * spaces[i]

    return seq


if __name__ == "__main__":
    print(part1('input1.txt'))
    print(part1('input2.txt'))
    print(part2('input1.txt'))
    print(part2('input2.txt'))
