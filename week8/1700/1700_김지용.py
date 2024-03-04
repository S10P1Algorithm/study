import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
order = list(map(int, input().split()))

d = dict()

for i in order:
    d.setdefault(i, 0)
    d[i] += 1

plug = set()
total_cnt = 0

for h in range(K):
    j = order[h]

    if j in plug:
        d[j] -= 1
    elif len(plug) < N:
        plug.add(j)
        d[j] -= 1
    else:
        min_cnt = K
        curr_min = 0

        for l in plug:
            if d[l] < min_cnt:
                curr_min = l
                min_cnt = d[l]
            elif d[l] == min_cnt:
                for h1 in range(h+1, K):
                    if order[h1] == curr_min:
                        curr_min = l
                        break
        plug.remove(curr_min)
        print('removed', curr_min)
        plug.add(j)
        d[j] -= 1

        total_cnt += 1
    print(j, plug, d, total_cnt)

print(total_cnt)