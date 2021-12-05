def solve(input):
    return count_lines(input), count_lines(input, False)
    
def get_bounds(line):
    tokens = line.split(' -> ')
    start = [int(n) for n in tokens[0].split(',')]
    end = [int(n) for n in tokens[1].split(',')]
    return start, end

def count_lines(lines, no_diag=True):
    grid = {}
    for line in lines:
        start, end = get_bounds(line)

        # For part 1, only deal with horizontal and vertical
        # For part 2, include diagonal lines
        if (start[0] != end[0] and start[1] != end[1]) and (no_diag or abs(end[0]-start[0]) != abs(end[1]-start[1])):
            continue

        steps = max(abs(start[0]-end[0]), abs(start[1]-end[1]))
        x_step = (end[0] - start[0]) // steps
        y_step = (end[1] - start[1]) // steps
        x_values = [start[0]]*(steps+1) if start[0] == end[0] else [start[0]+i*x_step for i in range(0, steps+1)]
        y_values = [start[1]]*(steps+1) if start[1] == end[1] else [start[1]+i*y_step for i in range(0, steps+1)]

        for x,y in [(x_values[i], y_values[i]) for i in range(0, steps+1)]:
            if (x, y) not in grid:
                grid[(x, y)] = 0
            grid[(x, y)] += 1
    
    return len([x for x in grid.values() if x > 1])