"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        acc_sum = 0
        count = 0
        for i in range(len(nums)):
            acc_sum += nums[i]
            if (acc_sum - k) in dic:
                count += dic[acc_sum - k]
            dic[acc_sum] += 1
            
        return count
            
                