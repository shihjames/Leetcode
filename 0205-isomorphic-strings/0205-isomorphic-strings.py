class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars = {}
        replaced = set()
        
        for i in range(len(s)):
            if s[i] not in chars:
                if t[i] not in replaced:
                    chars[s[i]] = t[i]
                    replaced.add(t[i])
                else:
                    return False
            else:
                if t[i] != chars[s[i]]:
                    return False
        
        return True

                