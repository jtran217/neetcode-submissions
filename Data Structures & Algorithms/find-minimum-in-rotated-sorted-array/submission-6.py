class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1
        current_min = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                current_min = min(current_min, nums[l])
                break
            
            m = (l+r)//2
            current_min = min(current_min, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return current_min
