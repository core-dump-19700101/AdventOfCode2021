def get_input_path(day, example=False):
    return 'config/day%s/input%s' % (day, '_ex' if example else '')

def get_input_str(day, example=False):
    input = None
    with open(get_input_path(day, example)) as f:
        input = f.read()
    return input

def get_input_lines(day, example=False):
    input = get_input_str(day, example)
    return input.splitlines() if input else None