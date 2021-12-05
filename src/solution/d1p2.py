def solve(input):
    window_size = 3
    i = 0
    prev_sum = -1
    count = 0
    while i <= len(input) - window_size:
        sum = 0
        for line in input[i:i+window_size]:
            sum += int(line)
        if prev_sum > -1 and sum > prev_sum:
            count += 1
        prev_sum = sum
        i += 1
    return count