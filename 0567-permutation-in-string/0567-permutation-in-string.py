"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        match = 0
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        
        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                match += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            index = ord(s2[right]) - ord("a")
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                match += 1
            elif s1_count[index] + 1 == s2_count[index]:
                match -= 1
            
            index = ord(s2[left]) - ord("a")
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                match += 1
            elif s1_count[index] - 1 == s2_count[index]:
                match -= 1
            
            left += 1
        
        return match == 26
            
                
                