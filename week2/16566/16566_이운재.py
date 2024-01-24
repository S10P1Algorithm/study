import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    x, y = find(a), find(b)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x

input = sys.stdin.readline

N, M, K = map(int, input().split())

parent = [i for i in range(N)]
minsu = list(map(int, input().split()))
chulsu = list(map(int, input().split()))

minsu.sort()


for i in chulsu:
    res = binary_search(minsu, i, 0, M-1)
    res = find(res)
    print(minsu[res])
    union(res, res+1)
    # del minsu[res]
    # print(minsu)
    # M -= 1

'''
문제를 보는 순간 입력범위를 보고 이진탐색을 해야한다는 것 까진 알아채렸다.
그래서 del을 이용해서 리스트 원소를 삭제하는 방식으로 했지만 시간초과가 났다.

그래서 검색한 결과 유니온 파인드 알고리즘을 결합해서 시간을 줄여주는것도 핵심이었다.
더 공부해야겠다.....

'''