class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur, index):
            res.append(cur[:])
            for i in range(index, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i+1)
                cur.pop()
                 
        res = []
        backtrack([], 0)
        return res