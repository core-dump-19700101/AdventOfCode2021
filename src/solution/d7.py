import math

def solve(input):
    positions = [int(n) for n in input[0].split(',')]
    return find_min_position(positions), find_min_position(positions, False)

def calc_fuel_cost(p, positions, linear=True):
    cost = 0
    for i in range(0, len(positions)):
        base_cost = abs(positions[i]-p)
        cost += base_cost if linear else base_cost * (base_cost+1) // 2
    return cost

def get_target_positions(positions, linear=True):
    if linear:
        return positions
    mean = sum(positions)/len(positions)
    return set([math.floor(mean), math.ceil(mean)])

def find_min_position(positions, linear=True):
    cache = {}
    min_p = None
    for p in get_target_positions(positions, linear):
        if p not in cache:
            cache[p] = calc_fuel_cost(p, positions, linear)
        if min_p == None or min_p[1] > cache[p]:
            min_p = (p, cache[p])
    return min_p[1]