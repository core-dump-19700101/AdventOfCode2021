from functools import reduce

def parse_file(file):
    result = []
    with open(file) as f:
        result = reduce(add_lines, f.readlines(), [0, 0])
    return result[0]*result[1]
            
def add_lines(line1, line2):
    parsed1 = line1 if isinstance(line1, list) else parse_line(line1)
    parsed2 = line2 if isinstance(line2, list) else parse_line(line2)
    return [parsed1[0]+parsed2[0], parsed1[1]+parsed2[1]]

def parse_line(line):
    result = [0, 0]
    if line == '\n':
        return result
    tokens = line.split()
    command = [tokens[0], int(tokens[1])]
    if command[0] == 'forward':
        result[0] += command[1]
    elif command[0] == 'up':
        result[1] -= command[1]
    elif command[0] == 'down':
        result[1] += command[1]
    return result

print(parse_file('day2/input'))