class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp1 = [0] + nums[:len(nums)-1]
        dp2 = [0] + nums[1:]
        
        print(dp1)
        print(dp2)
        
        for i in range(2, len(dp1)):
            dp1[i] = max(dp1[i-1], dp1[i] + dp1[i-2])
        
        for i in range(2, len(dp2)):
            dp2[i] = max(dp2[i-1], dp2[i] + dp2[i-2])
            
        return max(dp1[-1], dp2[-1])
        