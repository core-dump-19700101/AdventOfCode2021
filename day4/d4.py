import math
import re

class BingoBoard:
    def __init__(self, nums):
        self.nums = set(nums)

        dimension = int(math.sqrt(len(nums)))
        self.lines = []
        for i in range(0, dimension):
            # row
            self.lines.append(set(nums[i*dimension:i*dimension+dimension]))
            # col
            line = set()
            for j in range(0, dimension):
                line.add(nums[i+j*dimension])
            self.lines.append(line)

    def check(self, num):
        if num not in self.nums:
            return 0
        self.nums.remove(num)
        for line in self.lines:
            line.discard(num)
            if len(line) == 0:
                return sum([int(n) for n in self.nums])*int(num)
        return 0

    def __str__(self):
        return str(self.nums)

    def __repr__(self):
        return str(self)

def check_boards(boards, num):
    for board in boards:
        result = board.check(num)
        if result:
            return result
    return 0

def last_board(boards, num):
    won = []
    for board in boards:
        result = board.check(num)
        if result:
            if len(boards) == 1:
                return result
            won.append(board)
    if len(won) > 0:
        for board in won:
            boards.remove(board)
    return 0

called_nums = []
boards = []
with open('day4/input_test') as f:
    lines = f.read().splitlines()
    called_nums = lines[0].split(',')
    nums = []
    for line in lines[1:]:
        nums.extend(re.findall(r'\S+', line))
        if len(nums) == 25:
            boards.append(BingoBoard(nums))
            nums = []

    for num in called_nums:
        result = last_board(boards, num) # check_boards for part 1
        if result:
            print(result)
            break