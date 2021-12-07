CYCLE = 7
INITIAL = 8
DURATION_1 = 80
DURATION_2 = 256

def solve(input):
    fish_dict = build_fish_dict(input[0].split(','))
    return calc_population(dict(fish_dict), DURATION_1), calc_population(fish_dict, DURATION_2)

def build_fish_dict(fish):
    fish_dict = {}
    for day in fish:
        d = int(day)
        fish_dict[d] = fish_dict.get(d, 0) + 1
    return fish_dict

def get_spawns(days, duration):
    if days >= duration:
        return []
    spawns = []
    for i in range(0, (duration - days - 1) // CYCLE + 1):
        spawns.append(days+1 + CYCLE*i + INITIAL)
    return spawns

def calc_population(fish_dict, duration):
    cache = {}
    count = 0
    while len(fish_dict) > 0:
        day = list(fish_dict.keys())[0]
        value = fish_dict.pop(day)
        count += value
        spawns = cache.get(day, get_spawns(day, duration))
        cache[day] = spawns
        for spawn in spawns:
            fish_dict[spawn] = fish_dict.get(spawn, 0) + value
    return count