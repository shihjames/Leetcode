class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Dict = {} # key: num, value: index
        for i, num in enumerate(nums2):
          nums2Dict[num] = i

        # nums2 = [1, 3, 4, 2]
        # 		   i  j ->    
        # Step2:
        greaterList = [-1] * len(nums2)
        for i in range(len(nums2) - 1):
          currNum = nums2[i]
          for j in range(i + 1, len(nums2)):
            if currNum < nums2[j]:
              greaterList[i] = nums2[j]
              break

        # Step3:
        result = []
        for num in nums1:
          position = nums2Dict[num]
          result.append(greaterList[position])

        return result
            