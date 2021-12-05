from src.util import input_helper
from re import match
from os import listdir

class Solution:
    def __init__(self, filename, module):
        m = match(r'd(\d+)(?:p(\d+))?', filename)
        self.day = m.group(1)
        self.part = m.group(2) if m.group(2) else 0
        self.solve = module.solve    
    def run(self, input):
        if self.part:
            print('%s: %d' % (str(self), self.solve(input)))
        else:
            ans1, ans2 = self.solve(input)
            print('%s Part 1: %d' % (str(self), ans1))
            print('%s Part 2: %d' % (str(self), ans2))
    def __str__(self):
        if self.part:
            return 'Day %s Part %s' % (self.day, self.part)
        return 'Day %s' % (self.day)
    def __repr__(self):
        return str(self)

def get_solutions():
    solutions = []
    for f in listdir('./src/solution'):
        if not f.endswith('.py'):
            continue
        module = __import__('src.solution.%s' % (f.strip('.py')), fromlist=[None])
        solutions.append(Solution(f, module))
    return solutions

def main():
    solutions = get_solutions()
    for s in solutions:
        input = input_helper.get_input_lines(s.day, example=False)
        s.run(input)

if __name__ == '__main__':
    main()