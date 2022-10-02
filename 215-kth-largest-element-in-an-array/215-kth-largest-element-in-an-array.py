"""
Time = average: O(n), worst: O(n**2)
Space = O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left, right, target):
            if left == right:
                return nums[left]
            pivot_index = randint(left, right)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            i = right - 1
            for j in range(right-1, left-1, -1):
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i -= 1
            nums[right], nums[i+1] = nums[i+1], nums[right]
            pivot_index = i + 1
            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index > target:
                return quickSelect(left, pivot_index - 1, target)
            else:
                return quickSelect(pivot_index + 1, right, target)
                    
        return quickSelect(0, len(nums)-1, len(nums)-k)