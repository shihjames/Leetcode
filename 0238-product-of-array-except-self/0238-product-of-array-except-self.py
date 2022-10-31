class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        zeros = counter[0]
        if zeros >= 2:
            return [0] * len(nums)
        elif zeros == 1:
            product = 1
            zero_idx = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    product *= nums[i]
                    nums[i] = 0
                else:
                    zero_index = i
            nums[zero_index] = product
            return nums
        else:
            product = 1
            for i in range(len(nums)):
                product *= nums[i]
            for i in range(len(nums)):
                nums[i] = product // nums[i]
            return nums
                    