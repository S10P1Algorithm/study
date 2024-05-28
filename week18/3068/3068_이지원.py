def maximumValueSum(nums: list[int], k: int, edges: list[list[int]]) -> int:
    max_num = 0
    l = len(edges)
    
    for changed in range(1, 2 ** l):
        temp = 0
        copyed = [x for x in nums]
    
        for i in range(l):
    
            if changed & (1 << i):
                u, v = edges[i]
                temp -= copyed[u] + copyed[v]
                
                copyed[u] ^= k
                copyed[v] ^= k

                temp += copyed[u] + copyed[v]

        max_num = max(temp, max_num)

    return max_num + sum(nums)

# 시간 초과



class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        n=len(nums)
        def f(i, c):
            if i==n:
                if c==1: return -(1<<31)
                return 0
            x=nums[i]
            return max(x+f(i+1, c),(x^k)+f(i+1,1-c))
        return f(0, 0)