"""
Time = O(nlog(n))
Space = O(1)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        def qsort(s, e):
            if s < e:
                pivot = nums[random.randint(s,e)]
                i, j = s, e
                while i <= j:
                    while i <= j and nums[i] < pivot:
                        i += 1
                    while i <= j and nums[j] > pivot:
                        j -= 1
                    if i <= j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1
                qsort(s, j)
                qsort(i, e)
        qsort(0, len(nums) - 1)
        return nums