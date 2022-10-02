"""
Time = O(nlog(n))
Space = O(log(n))
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        def qsort(start, end):
            if start < end:
                pivot = nums[random.randint(start, end)]
                i, j = start, end
                while i <= j:
                    while i <= j and nums[i] < pivot:
                        i += 1
                    while i <= j and nums[j] > pivot:
                        j -= 1
                    if i <= j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1
                qsort(start, j)
                qsort(i, end)
        qsort(0, len(nums) - 1)
        return nums