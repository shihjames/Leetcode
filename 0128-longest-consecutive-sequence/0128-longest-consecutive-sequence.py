class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_num = max(nums)
        min_num = min(nums)
        longest = float("-inf")
        for i in range(len(nums)):
            cur = nums[i]
            cur_length = 1
            if cur in nums_set:
                left, right = cur-1, cur+1
                while left >= min_num:
                    if left in nums_set:
                        cur_length += 1
                        nums_set.remove(left)
                        left -= 1
                    else:
                        break
                while right <= max_num:
                    if right in nums_set:
                        cur_length += 1
                        nums_set.remove(right)
                        right += 1
                    else:
                        break
            longest = max(longest, cur_length)
        return longest