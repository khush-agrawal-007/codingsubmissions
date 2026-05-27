class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Arrays to store boundary indices for 26 letters
        last_lower = [-1] * 26
        first_upper = [-1] * 26
        
        for i, char in enumerate(word):
            if char.islower():
                # Continuously update to keep the last seen index
                last_lower[ord(char) - ord('a')] = i
            else:
                # Only update if it's the very first time seeing this uppercase letter
                idx = ord(char) - ord('A')
                if first_upper[idx] == -1:
                    first_upper[idx] = i
                    
        special_count = 0
        
        for i in range(26):
            # Check if both cases exist and the order condition is satisfied
            if last_lower[i] != -1 and first_upper[i] != -1:
                if last_lower[i] < first_upper[i]:
                    special_count += 1
                    
        return special_count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna