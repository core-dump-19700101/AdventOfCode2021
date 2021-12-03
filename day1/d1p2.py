WINDOW_SIZE = 3

with open('day1/input') as f:
    lines = f.readlines()
    i = 0
    prev_sum = -1
    count = 0
    while i <= len(lines) - WINDOW_SIZE:
        sum = 0
        for line in lines[i:i+WINDOW_SIZE]:
            sum += int(line)
        if prev_sum > -1 and sum > prev_sum:
            count += 1
        prev_sum = sum
        i += 1
    print(count)