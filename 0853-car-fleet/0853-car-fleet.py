"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        # Sort the list
        pos_speed.sort()
        
        stack = []
        
        # Traverse the pos_speed list reversely
        for pos, speed in pos_speed[::-1]:
            # Calculate the time needed for current car to reach target
            time = (target - pos) / speed
            # Found car that can reach the car in its front
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
        