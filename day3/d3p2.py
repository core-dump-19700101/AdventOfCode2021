import math

class BitTrie:
    def __init__(self, val=0):
        self.zero = None
        self.one = None
        self.count = 0
        self.val = val

def build_bit_trie(lines):
    head = BitTrie()
    depth = len(lines[0]) - 1
    for line in lines:
        node = head
        for i in range(0, depth):
            node.count += 1
            if line[i] == '0':
                if not node.zero:
                    node.zero = BitTrie()
                node = node.zero
            else:
                if not node.one:
                    node.one = BitTrie(int(math.pow(2, depth-i-1)))
                node = node.one
    return head

def compute_rating(trie, compare):
    node = trie
    rating = 0
    while node.zero != None or node.one != None:
        if node.count == 1:
            node = node.zero if node.zero != None else node.one
        else:
            node = node.zero if compare(node.zero.count, node.one.count) else node.one
        rating += node.val
    return rating

with open('day3/input') as f:
    lines = f.readlines()
    bitwise_trie = build_bit_trie(lines)
    o2 = compute_rating(bitwise_trie, lambda a,b: a>b)
    co2 = compute_rating(bitwise_trie, lambda a,b: a<=b)
    print("o2=%d, co2=%d, o2*co2=%d" % (o2, co2, o2 * co2))