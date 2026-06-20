class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # ------------------------------------------------------------
        # LeetHub AI Coach Review:
        # This implementation follows the standard O(m log m) approach:
        #   1. Add implicit boundaries (building 1 height 0, building n
        #      with a very high height) and sort the restrictions.
        #   2. Perform a forward pass to enforce the maximum increase
        #      of 1 per building moving left‑to‑right.
        #   3. Perform a backward pass to enforce the same constraint
        #      moving right‑to‑left.
        #   4. For each adjacent pair of restricted buildings, the
        #      highest possible peak lies halfway between them, given
        #      the distance and their heights. Compute this peak and
        #      keep the maximum.
        # Time Complexity: O(m log m) where m = len(restrictions) + 2
        #   (sorting dominates). The forward/backward passes are O(m).
        # Space Complexity: O(m) for storing the modified restrictions.
        # The solution is optimal for this problem; no further
        # asymptotic improvement is possible.
        # ------------------------------------------------------------

        # 1. Add implicit boundary restrictions and sort
        restrictions.append([1, 0])
        restrictions.append([n, 10**9])
        restrictions.sort()
        
        m = len(restrictions)
        
        # 2. Forward Pass: Propagate constraints from left to right
        for i in range(1, m):
            id_curr, h_curr = restrictions[i]
            id_prev, h_prev = restrictions[i-1]
            # Height at current building cannot exceed height at previous
            # building plus the distance between them (max slope = 1)
            restrictions[i][1] = min(h_curr, h_prev + (id_curr - id_prev))
            
        # 3. Backward Pass: Propagate constraints from right to left
        for i in range(m - 2, -1, -1):
            id_curr, h_curr = restrictions[i]
            id_next, h_next = restrictions[i+1]
            # Symmetrically enforce the slope constraint from the right side
            restrictions[i][1] = min(h_curr, h_next + (id_next - id_curr))
            
        # 4. Calculate the max peak height between every adjacent pair
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            # The highest possible building between id1 and id2 is achieved
            # when the heights increase as fast as possible from both ends
            # and meet in the middle.
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna