from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        missing = []
        
        for i in range(1, len(nums) + 1):
            if i not in counter:
                missing.append(i)
        
        return missing