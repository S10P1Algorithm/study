import sys
sys.stdin = open("input.txt", "r")

class Node():
    def __init__(self, key, depth = -1):
        self.key = key
        self.children = {}
        self.depth = depth
        self.is_visited = False

class Trie():
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        node = self.head

        _path = list(string.split("\\"))
        for folder in _path:
            if folder not in node.children:
                current_depth = node.depth
                node.children[folder] = Node(folder, depth=current_depth+1)
            node = node.children[folder]
        return node


N = int(input())
A = Trie()

for _ in range(N):
    A.insert(input())

stack = []
A.head.is_visited = True
A.head.children
stack.append(A.head)

while stack:
    current_node = stack[-1]

    for key in sorted(current_node.children.keys()):
        child_node = current_node.children[key]
        if not child_node.is_visited:
            child_node.is_visited = True
            stack.append(child_node)
            for _ in range(child_node.depth):
                print(" ", end="")
            print(child_node.key)
            break
    else:
        stack.pop()
