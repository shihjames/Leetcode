class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def quickSelect(left, right):
            if left == right:
                return
            pivot_index = randint(left, right)
            pivot = unique[pivot_index][0]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            i = left
            for j in range(left, right):
                if unique[j][0] >= pivot:
                    unique[i], unique[j] = unique[j], unique[i]
                    i += 1
            unique[right], unique[i] = unique[i], unique[right]
            pivot_index = i
            if pivot_index == k:
                return
            elif pivot_index > k:
                return quickSelect(left, pivot_index-1)
            else:
                return quickSelect(pivot_index+1, right)
                              
        k -= 1
        counter = Counter(nums)
        unique = [(count, num) for num, count in counter.items()]
        quickSelect(0, len(unique)-1)
        return [num for count, num in unique[:k+1]]