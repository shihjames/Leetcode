"""
Time = O(n**2)
Space = O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findComb(index):
            left = index + 1
            right = len(nums) - 1
            
            # Traverse numbers after current num
            while left < right:
                # Count the sum of the combination
                total = nums[index] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
            
        nums.sort()
        res = []
        # Traverse through the array
        for i in range(len(nums)):
            # Break if its larger than 0
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            findComb(i)
        
        return res
            