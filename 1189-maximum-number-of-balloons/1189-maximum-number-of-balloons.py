from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_dicT = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        counter = Counter(text)
        max_num = float("inf")
        
        for char in char_dicT:
            if char not in counter:
                return 0
            max_num = min(max_num, counter[char] // char_dicT[char])
                
        return max_num