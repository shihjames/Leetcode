class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = [0] * len(arr)
        cur_max[-1] = arr[-1]
        
        for i in range(len(arr)-2, -1, -1):
            cur_max[i] = max(cur_max[i+1], arr[i])
        
        for i in range(len(arr) - 1):
            arr[i] = cur_max[i + 1]
        
        arr[-1] = -1
        
        return arr