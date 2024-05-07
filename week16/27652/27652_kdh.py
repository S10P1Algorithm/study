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
    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        
        return len(words)
    
    def delete(self, string):
        node = self.head
        stack = []
        for char in string:
            if char in node.children:
                node = node.children[char]
                stack.append(node)
            else:
                return None
        while stack:
            node =stack.pop()
            if len(node.children) == 0:
                node.data = None
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
            new_text = ''.join(reversed(text))
            B.insert(new_text)

    elif command == "delete":
        destination = input_list[0]
        text = input_list[1]
        if destination == "A":
            A.delete(text)
        else:
            new_text = ''.join(reversed(text))
            B.delete(new_text)
            
    elif command == "find":
        text = input_list[0]
        N = len(text)
        ans = 0
        for i in range(1, N):
            prefix = text[:i]
            suffix = ''.join(reversed(text[i:]))
            if A.starts_with(prefix) and B.starts_with(suffix):
                ans += A.starts_with(prefix) * B.starts_with(suffix)
        print(ans)
    else:
        pass
