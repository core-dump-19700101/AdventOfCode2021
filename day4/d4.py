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

        self.score = 0

    def check(self, num):
        if num not in self.nums:
            return False
        self.nums.remove(num)
        for line in self.lines:
            line.discard(num)
            if len(line) == 0:
                self.score = sum([int(n) for n in self.nums])*int(num)
                return True
        return False

def get_winners(boards, num):
    won = []
    for board in boards:
        result = board.check(num)
        if result:
            won.append(board)
    if len(won) > 0:
        for board in won:
            boards.remove(board)
    return won

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

    winners = []
    for num in called_nums:
        winners.extend(get_winners(boards, num))

    print(winners[0].score)
    print(winners[-1].score)