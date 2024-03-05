import sys

input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))

d = dict()

# 각강의 숫자가 나오는 횟수를 저장
for i in order:
    d.setdefault(i, 0)
    d[i] += 1

# 전기콘센트와 결괏값
plug = set()
total_cnt = 0

# 부여된 순서대로 탐색
# 세가지 경우의 수
# 1. 이미 꽂혀 있는 경우
# 2. 빈 콘센트가 있는 경우
# 3. 빈 콘센트가 없고 이미 꽂혀 있지 않은 경우
for h in range(K):
    j = order[h]
    
    # 1번 경우
    if j in plug:
        d[j] -= 1
    
    # 2번 경우
    elif len(plug) < N:
        plug.add(j)
        d[j] -= 1
    
    # 3번 경우
    # 뒤에서 더 이상 안쓰는 것이 있으면 그걸 뽑음
    # 모두 다 뒤에 사용하면 가장 나중에 사용하는 걸 뽑음
    else:
        visited = set()
        for h1 in range(h+1, K):
            curr_next = order[h1]
            if curr_next in plug and curr_next not in visited:
                curr_min = curr_next
                visited.add(curr_next)

        for l in plug:
            if d[l] == 0:
                curr_min = l

        plug.remove(curr_min)

        plug.add(j)
        d[j] -= 1

        total_cnt += 1

print(total_cnt)
