count = 0
prev_depth = -1
with open('day1/input') as f:
    line = f.readline()
    while line:
        depth = int(line)
        if (prev_depth > -1 and depth > prev_depth):
            count += 1
        prev_depth = depth
        line = f.readline()

print("Increased " + str(count) + " times")