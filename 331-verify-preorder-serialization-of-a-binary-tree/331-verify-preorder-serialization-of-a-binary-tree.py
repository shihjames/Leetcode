"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        spaceCount = 1
        for node in preorder:
            spaceCount -= 1
            if spaceCount < 0:
                return False
            if node != "#":
                spaceCount += 2
        return not spaceCount