import itertools
import math

def solution(n, weak, dist):
    weak_size = len(weak)
    weak = weak + [w + n for w in weak]
    mininum = math.inf
    for start in range(weak_size):
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weak_size):
                next_pos = start + i
                diff = weak[next_pos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = next_pos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                mininum = min(mininum, cnt)
    if mininum == math.inf:
        return -1
    
    return mininum