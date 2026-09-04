class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueChar = set(s)
        maxCount = 0
        for c in uniqueChar:
            l = count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                maxCount = max(maxCount,r-l+1)
        return maxCount