def solution(n, weak, dist):
    dist.sort()
    gap = []
    lw = len(weak)
    ld = len(dist)
    for i in range(lw - 1):
        gap.append(weak[i + 1] - weak[i])
        
    gap.append(n + weak[0] - weak[lw - 1])
    
    def recursion(exc=0, k=0, start=0):
        if k > ld:
            return k
        
        if k > 0:
            part = []
            temp = 0
            
            for i in range(lw):
                if (exc & (1 << i)):
                    part.append(temp)
                    temp = 0
            
                else:
                    temp += gap[i]
            
            if temp != 0:
                part[0] += temp
            
            part.sort(reverse=True)
            
            for i, p in enumerate(part):
                if p > dist[ld - 1 - i]:
                    break
            else:
                return k    
            
        result = ld + 1
        
        for i in range(start, lw):
            if not (exc & (1 << i)):
                result = min(recursion(exc | (1 << i), k+1, i+1), result)

        
        return result
    
    answer = recursion()

    if answer > ld:
        answer = -1
    return answer

print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))