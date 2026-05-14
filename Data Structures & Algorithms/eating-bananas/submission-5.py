class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min k such that eat all bananas within h hours
        # max k is highest pile in piles

        l,r = 1, max(piles)
        min_k = max(piles)
        while l<=r:
            k = (l + r) // 2
            current_h = 0 

            for pile in piles:
                current_h += math.ceil(float(pile)/k)
            if current_h <= h :
                min_k = k
                r = k - 1
            else:
                l = k + 1
        
        return min_k




