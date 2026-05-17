from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])
        
        while queue:
            curr = queue.popleft()
            
            # If we land on a 0, we've successfully reached our goal
            if arr[curr] == 0:
                return True
            
            # Explore jumping left and right
            jump = arr[curr]
            for next_pos in (curr - jump, curr + jump):
                # Ensure the jump stays within array bounds and hasn't been visited
                if 0 <= next_pos < len(arr) and next_pos not in visited:
                    visited.add(next_pos)
                    queue.append(next_pos)
                    
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna