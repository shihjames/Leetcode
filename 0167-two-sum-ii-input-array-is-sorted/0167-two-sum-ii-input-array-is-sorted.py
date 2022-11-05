"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left = 0
        right = len(numbers) - 1
        
        # Traverse from the leftmost and the rightmost
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            # Sum is equals to the target
            if cur_sum == target:
                return [left + 1, right + 1]
            # Sum is smaller than the target
            elif cur_sum < target:
                left += 1
            # Sum is larger than the target
            else:
                right -= 1
        
        return [-1, -1]