class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        # Step 1: Store all prefixes from arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
                
        longest = 0
        
        # Step 2: Check prefixes of arr2 against the set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # Found a match! Calculate length using string conversion
                    # and break because smaller prefixes will be shorter.
                    longest = max(longest, len(str(num)))
                    break
                num //= 10
                
        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna