class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = [0] * 26

        for c in word:
            if 'a' <= c <= 'z':
                res[ord(c) - ord('a')] |= 1
            else:
                res[ord(c) - ord('A')] |= 2

        return sum(x == 3 for x in res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna