class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l<=r:
            t_times = 0
            k = (l+r) // 2
            for pile in piles:
                t_times += math.ceil(float(pile)/k)
            if t_times <= h:
                r = k - 1
                res = k
            else:
                l = k + 1 
        return res
