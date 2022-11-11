class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        start = False
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and not start:
                continue
            elif s[i] == " " and start:
                return length
            else:
                start = True
                length += 1
        
        return length