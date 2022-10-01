"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left, right, bound):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if bound == "l":
                        if mid != 0 and nums[mid] == nums[mid-1]:
                            right = mid - 1
                        else:
                            return mid
                    else:
                        if mid != len(nums)-1 and nums[mid] == nums[mid+1]:
                            left = mid + 1
                        else:
                            return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        left, right = 0, len(nums) - 1
        low = binarySearch(left, right, "l")
        if low == -1:
            return [-1, -1]
        else:
            high = binarySearch(left, right, "h")
            return [low, high]