class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        count = 0

        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)

            if freq.get(lower, 0) > 0 and freq.get(upper, 0) > 0:
                count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna