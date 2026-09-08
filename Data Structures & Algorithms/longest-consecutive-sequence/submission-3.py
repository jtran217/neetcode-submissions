class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        maxCount = 0
        for num in uniqueNums:
            if num-1 not in uniqueNums:
                count = 1
                while num + count in uniqueNums:
                    count +=1
                maxCount = max(maxCount,count)
        return maxCount
