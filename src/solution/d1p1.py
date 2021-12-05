def solve(input):
    count = 0
    prev_depth = -1
    for line in input:
        depth = int(line)
        if (prev_depth > -1 and depth > prev_depth):
            count += 1
        prev_depth = depth
    return count