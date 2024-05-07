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

Q = int(input())
A = Trie()
B = Trie()

for _ in range(Q):
    command, *input_list = sys.stdin.readline().split()
    if command == "add":
        destination = input_list[0]
        text = input_list[1]
        if destination == "A":
            A.insert(text)
        else:
            B.insert(text)

    elif command == "delete":
        destination = input_list[0]
        text = input_list[1]
        if destination == "A":
            A.insert(text)
        else:
            B.insert(text)
            
    elif command == "find":
        pass
    else:
        pass
