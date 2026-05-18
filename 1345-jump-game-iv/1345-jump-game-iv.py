from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Base case: if the array has 1 or 0 elements, 0 jumps are needed
        if n <= 1:
            return 0
            
        # Create a graph mapping each value to a list of its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # Initialize BFS
        queue = deque([0])  # Start at index 0
        visited = {0}       # Keep track of visited indices
        steps = 0
        
        while queue:
            # Process all nodes at the current depth level
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                
                # If we have reached the last index, return the number of steps
                if node == n - 1:
                    return steps
                    
                # Explore the 3 possible types of jumps:
                
                # 1. Jump forward (i + 1)
                if node + 1 < n and (node + 1) not in visited:
                    visited.add(node + 1)
                    queue.append(node + 1)
                    
                # 2. Jump backward (i - 1)
                if node - 1 >= 0 and (node - 1) not in visited:
                    visited.add(node - 1)
                    queue.append(node - 1)
                    
                # 3. Jump to any index j where arr[i] == arr[j]
                for neighbor in graph[arr[node]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                
                # OPTIMIZATION: Clear the list for this value in the graph.
                # Once we've added these teleportation neighbors to the queue, 
                # we never need to check this value's list again.
                graph[arr[node]].clear()
                
            # Increment steps after exploring all nodes at the current level
            steps += 1
            
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna