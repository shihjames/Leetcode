class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set()
        sum_dict = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1, len(nums)):
                    complement = -(nums[i] + nums[j])
                    if complement in sum_dict and sum_dict[complement] == i:
                        res.add(tuple(sorted([nums[i], nums[j], complement])))
                    sum_dict[nums[j]] = i
        return res