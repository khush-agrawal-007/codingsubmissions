from typing import List
from sortedcontainers import SortedList

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * size

    def maximize(self, i, val):
        # Update the tree with a new maximum value
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def query(self, i):
        # Retrieve the maximum value up to index i
        res = 0
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & -i
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Based on constraints: 1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
        MAX_X = 50005 
        
        tree = FenwickTree(MAX_X + 1)
        # Initialize with sentinel values: origin (0) and infinity limit (MAX_X)
        obstacles = SortedList([0, MAX_X]) 
        
        # 1. Forward pass: Build the final state by adding all obstacles
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])
                
        # 2. Initialize the Fenwick tree with the final state's gaps
        # We record the gap x2 - x1 at the right-most point, x2
        prev = obstacles[0]
        for i in range(1, len(obstacles)):
            curr = obstacles[i]
            tree.maximize(curr, curr - prev)
            prev = curr
            
        ans = []
        
        # 3. Process queries backwards
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                idx = obstacles.index(x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx + 1]
                
                # Time reversal: Removing 'x' merges two gaps into one larger one.
                # The new gap ends at next_obs and spans back to prev_obs.
                tree.maximize(next_obs, next_obs - prev_obs)
                obstacles.remove(x)
            else:
                x = q[1]
                sz = q[2]
                
                # Find the largest obstacle that is <= x
                idx = obstacles.bisect_right(x) - 1
                prev_obs = obstacles[idx]
                
                # The max possible space is the max of:
                # - Any fully formed gap ending at or before prev_obs
                # - The trailing space between prev_obs and the query limit x
                max_completed_gap = tree.query(prev_obs)
                
                if max_completed_gap >= sz or (x - prev_obs) >= sz:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        # 4. We collected answers backwards, so return them forwards
        return ans[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna