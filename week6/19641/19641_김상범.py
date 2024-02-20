from collections import defaultdict

relatedList = defaultdict(list)
leftlist = [0] * 100001
rightlist = [0] * 100001

def dfs(node, val):
    leftlist[node] = val
    for i in relatedList[node]:
        if not leftlist[i]:
            val = dfs(i, val + 1)
    rightlist[node] = val + 1
    return val + 1

def main():
    N = int(input())

    for _ in range(N):
        n, *connections = map(int, input().split())
        for c in connections:
            if c == -1:
                break
            relatedList[n].append(c)
        relatedList[n].sort()

    s = int(input())
    dfs(s, 1)
    for i in range(1, N + 1):
        print(i, leftlist[i], rightlist[i])

if __name__ == "__main__":
    main()
