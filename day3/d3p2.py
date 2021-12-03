class BTrie:
    def __init__(self, val=0):
        self.zero = None
        self.one = None
        self.count = 0
        self.val = val

def build_trie(lines):
    head = BTrie()
    depth = len(lines[0]) - 1
    for line in lines:
        node = head
        for i in range(0, depth):
            node.count += 1
            if line[i] == '0':
                if not node.zero:
                    node.zero = BTrie()
                node = node.zero
            else:
                if not node.one:
                    node.one = BTrie(2**(depth-i-1))
                node = node.one
    return head

def calc_rating(trie, compare):
    node = trie
    rating = 0
    while node.count > 0:
        if node.count == 1:
            node = node.zero if node.zero != None else node.one
        else:
            node = node.zero if compare(node.zero.count, node.one.count) else node.one
        rating += node.val
    return int(rating)

with open('day3/input') as f:
    t = build_trie(f.readlines())
    print(calc_rating(t, lambda a,b: a>b) * calc_rating(t, lambda a,b: a<=b))