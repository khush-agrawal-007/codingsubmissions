class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        # Forward pass to calculate the total length
        for c in s:
            if c == '*':
                m = max(0, m - 1)
            elif c == '#':
                m *= 2
            elif c != '%':
                m += 1
                
        # If k is out of bounds of the final string
        if k >= m:
            return "."
            
        # Backward pass to trace the origin of the k-th character
        for c in reversed(s):
            if c == '*':
                m += 1
            elif c == '#':
                m //= 2
                # If k is in the duplicated half, map it back to the first half
                if k >= m:
                    k -= m
            elif c == '%':
                # Map the index to its position before reversal
                k = m - 1 - k
            else:
                m -= 1
                # If the current character is the one that landed at k, we found it!
                if k == m:
                    return c
                    
        return "."

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna