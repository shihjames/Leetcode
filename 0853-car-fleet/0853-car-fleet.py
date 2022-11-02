"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        # Create position and speed pair
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort()
        
        # Store car fleet(s)
        stack = []
        
        # Reverse sorted order
        for pos, speed in pos_speed[::-1]:
            time = (target - pos) / speed
            # Check if there is a collision
            if len(stack) >= 1 and time <= stack[-1]:
                continue
            # Stack is empty or no collision
            else:
                stack.append(time)
                
        return len(stack)
            
                
        
        