"""
Time = O(m*n)
Space = O(m*n)
where n is the length of coins, m is the amount
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(index, cur_amount):
            if cur_amount == amount:
                return 1
            if cur_amount > amount:
                return 0
            if index == len(coins):
                return 0
            if (index, cur_amount) in memo:
                return memo[(index, cur_amount)]
            
            memo[(index, cur_amount)] = dfs(index, cur_amount + coins[index]) + dfs(index + 1, cur_amount)
            return memo[(index, cur_amount)]
        
        return dfs(0, 0)