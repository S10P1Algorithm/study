class NonOverlappingSet:
    def __init__(self, m):
        self.parents = [i for i in range(m)]

    def find(self, k):
        if k == self.parents[k]:
            return k
        self.parents[k] = self.find(self.parents[k])
        return self.parents[k]

    def union(self, m, n):
        x = self.find(m)
        y = self.find(n)

        if x == y:
            return

        self.parents[y] = x


Cardset = []

def main():
    global Cardset

    N, M, K = map(int, input().split())

    Cardset = list(map(int, input().split()))

    act = NonOverlappingSet(N + 1)
    Cardset.sort()
    q_list = list(map(int, input().split()))
    for _ in range(K):
        q = q_list[_]
        start, end = 0, M - 1

        while start < end:
            mid = (start + end) // 2
            if act.find(Cardset[mid]) <= q:
                start = mid + 1
            else:
                end = mid

        print(act.find(Cardset[end]))

        if end == 0:
            act.union(0, Cardset[end])
        else:
            act.union(Cardset[end - 1], Cardset[end])


if __name__ == "__main__":
    main()
