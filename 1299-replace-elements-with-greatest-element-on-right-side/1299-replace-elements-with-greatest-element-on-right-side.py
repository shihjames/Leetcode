
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        arr[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1):
            new_value = cur_max
            cur_max = max(cur_max, arr[i])
            arr[i] = new_value

        return arr