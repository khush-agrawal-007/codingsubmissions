class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # 1. Add implicit boundary restrictions and sort
        restrictions.append([1, 0])
        restrictions.append([n, 10**9])
        restrictions.sort()
        
        m = len(restrictions)
        
        # 2. Forward Pass: Propagate constraints from left to right
        for i in range(1, m):
            id_curr, h_curr = restrictions[i]
            id_prev, h_prev = restrictions[i-1]
            restrictions[i][1] = min(h_curr, h_prev + (id_curr - id_prev))
            
        # 3. Backward Pass: Propagate constraints from right to left
        for i in range(m - 2, -1, -1):
            id_curr, h_curr = restrictions[i]
            id_next, h_next = restrictions[i+1]
            restrictions[i][1] = min(h_curr, h_next + (id_next - id_curr))
            
        # 4. Calculate the max peak height between every adjacent pair
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna