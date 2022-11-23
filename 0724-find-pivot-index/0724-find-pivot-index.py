class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        
        for i in range(len(nums)):
            if i == 0:
                if (total - nums[i]) / 2 == 0:
                    return i
            else:
                cur += nums[i-1]
                if cur == (total - nums[i]) / 2:
                    return i
        
        return -1