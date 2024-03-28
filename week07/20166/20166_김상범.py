dx = [1, 0, -1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
M = 0
N = 0
K = 0
jigoku = [[0 for _ in range(10)] for _ in range(10)]

class Node:
    def __init__(self, chr):
        self.chr = chr
        self.count = 1

class Trie:
    def __init__(self, chr, i, j):
        self.Head = Node(chr)
        self.cords = [(i, j)]
        self.child = []

    def search(self, s):
        if len(s) == 0:
            return self.Head.count

        for i in self.child:
            if i.Head.chr == s[0]:
                return i.search(s[1:])

        for j in self.cords:
            for k in range(8):
                nx = (j[0] + dx[k]) % M
                ny = (j[1] + dy[k]) % N
                self.insert(jigoku[nx][ny], nx, ny)

        for i in self.child:
            if i.Head.chr == s[0]:
                return i.search(s[1:])

        return 0

    def insert(self, s, x, y):
        for i in self.child:
            if i.Head.chr == s:
                i.cords.append((x, y))
                i.Head.count += 1
                return

        self.child.append(Trie(s, x, y))


if __name__ == "__main__":
    M, N, K = map(int, input().split())
    head = Trie(' ', 1000, 1000)

    for i in range(M):
        s = input().strip()
        for j in range(N):
            jigoku[i][j] = s[j]
            head.insert(jigoku[i][j], i, j)

    for _ in range(K):
        s = input().strip()
        print(head.search(s))
