import sys
sys.stdin = open("input.txt", "r")
class Node(object):
    def __init__(self, key, data=None):
        self.data = data
        self.key = key
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        node = self.head
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.data = string
        return node


t = int(input())
for _ in range(t):
    trie = Trie()
    n = int(input())

    leaf_check = []
    for i in range(n):
        leaf_check.append(trie.insert(sys.stdin.readline().strip()))
    
    for node in leaf_check:
        if node.children:
            print("NO")
            break
    else:
        print("YES")