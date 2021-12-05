def solve(input):
    position = [0, 0, 0]
    for line in input:
        position = calculate_position(parse_line(line), position)
    return position[0]*position[1]

def parse_line(line):
    tokens = line.split()
    return [tokens[0], int(tokens[1])]

def calculate_position(command, current_position):
    x = current_position[0]
    y = current_position[1]
    aim = current_position[2]
    if (command[0] == 'up'):
        aim -= command[1]
    elif (command[0] == 'down'):
        aim += command[1]
    elif (command[0] == 'forward'):
        x += command[1]
        y += command[1] * aim
    return [x, y, aim]