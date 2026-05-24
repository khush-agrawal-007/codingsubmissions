class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        memo = {}
        
        def dfs(i: int) -> int:
            # Return cached result if already computed
            if i in memo:
                return memo[i]
            
            max_jumps = 1
            
            # Look Right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal building
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            # Look Left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal building
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            # Cache and return
            memo[i] = max_jumps
            return max_jumps

        # Calculate DFS for every possible starting index and take the max
        return max(dfs(i) for i in range(n))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna