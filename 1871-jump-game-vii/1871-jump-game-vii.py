class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Optimization: If the last character is '1', we can never land on it.
        if s[-1] == '1':
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        # Tracks how many reachable indices are currently in our valid window
        available_jumps = 0
        
        for i in range(1, n):
            # 1. Add the index that just entered our valid jump window
            if i >= minJump and dp[i - minJump]:
                available_jumps += 1
                
            # 2. Remove the index that just fell out of our valid jump window
            if i > maxJump and dp[i - maxJump - 1]:
                available_jumps -= 1
                
            # 3. If we have at least one valid jump point and the current spot is '0'
            if available_jumps > 0 and s[i] == '0':
                dp[i] = True
                
        # The result is whether we could reach the last index
        return dp[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna