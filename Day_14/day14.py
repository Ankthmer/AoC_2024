import re

def part1(filename, wide, tall, time):
    '''Solution day 14 part 1'''

    #Pars the input
    robots = get_robot(filename)
    #Evolve the situation
    for rob in robots:
        rob.x = (rob.x + (time * rob.vx)) % wide
        rob.y = (rob.y + (time * rob.vy)) % tall

    #Calculate the safety index multipling the number of robot in each quadrant.

    return safey_index(robots, wide, tall)

class Robot:
    '''Represent a robot with is current position (x,y) and is velocity vector (vx, vy)'''
    def __init__(self, x, y, vx, vy):
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)

def get_robot(filename):
    '''Read the file and extract the informations about the initial position and velocity of all the robots'''

    with open(filename) as f:

        robots = []

        for line in f:
            #For every line extrapolate all the numbers with their sign, suppose that the order is always x, y, vx, vy.
            r = re.findall(r'-?\d\d*', line)
            #Create a new robot with the previusly founded numbers.
            a = Robot(*r)
            #Add him to the list.
            robots.append(a)

        return robots

def safey_index(robots, wide, tall):
    '''Calculate the safety index multipling the number of robot in each quadrant.'''
    #Initialize the counters.
    quad_1 = 0
    quad_2 = 0
    quad_3 = 0
    quad_4 = 0

    #Assign all robots to their quadrant.
    for rob in robots:
        if rob.x < int(wide/2):
            if rob.y < int(tall/2):
                quad_1 += 1
            elif rob.y > int(tall/2):
                quad_3 += 1
        elif rob.x > int(wide/2):
            if rob.y < int(tall/2):
                quad_2 += 1
            elif rob.y > int(tall/2):
                quad_4 += 1


    #Multiply the number of robots in each quadrant.
    return quad_1*quad_2*quad_3*quad_4







if __name__ == "__main__":
    print(part1('input1.txt', 11, 7, 100))
    print(part1('input2.txt', 101, 103, 100))
    #print(part2('input1.txt'))
    #print(part2('input2.txt'))
