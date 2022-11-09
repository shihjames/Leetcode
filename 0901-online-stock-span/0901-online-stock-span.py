"""
Time = O(1)
Space = O(n)
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
        else:
            count = 0
            while self.stack and self.stack[-1][0] <= price:
                count += self.stack.pop()[1]
            self.stack.append((price, count+1))
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)