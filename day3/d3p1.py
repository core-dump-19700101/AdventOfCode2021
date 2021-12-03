import math

def build_bit_frequency(lines):
    dict = {}
    for line in lines:
        for i in range(0, len(line) - 1):
            if i not in dict:
                dict[i] = [0, 0]
            dict[i][int(line[i])] += 1
    return dict

def calc_gamma_epsilon(frequency):
    gamma = 0
    epsilon = 0
    digits = len(frequency)
    for k, v in frequency.items():
        val = int(math.pow(2, digits - k - 1))
        if v[0] > v[1]:
            epsilon += val
        else:
            gamma += val
    return [gamma, epsilon]

with open('day3/input') as f:
    lines = f.readlines()
    gamma, epsilon = calc_gamma_epsilon(build_bit_frequency(lines))
    print(gamma * epsilon)