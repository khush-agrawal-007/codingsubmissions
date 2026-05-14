class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if max(nums) != len(nums)-1:
            return False
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i]!= i+1:
                return False
        if nums[-1] != n-1:
            return False
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna