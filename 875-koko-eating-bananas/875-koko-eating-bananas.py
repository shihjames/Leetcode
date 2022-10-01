class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minAmount = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)
            if time > h:
                left = mid + 1
            else:
                minAmount = min(minAmount, mid)
                right = mid - 1
        return minAmount