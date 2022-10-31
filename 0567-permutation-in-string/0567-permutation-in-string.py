"""
Time O(26) + O(n) = O(n)
Space = O(26) = O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_1 = [0] * 26
        count_2 = [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            count_1[ord(s1[i]) - ord("a")] += 1
            count_2[ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
            if count_1[i] == count_2[i]:
                matches += 1
                
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord("a")
            count_2[index] += 1
            if count_1[index] == count_2[index]:
                matches += 1
            elif count_1[index] + 1 == count_2[index]:
                matches -= 1
        
            index = ord(s2[left]) - ord("a")
            count_2[index] -= 1
            if count_1[index] == count_2[index]:
                matches += 1
            elif count_1[index] - 1 == count_2[index]:
                matches -= 1
                
            left += 1
        
        return matches == 26
            
                