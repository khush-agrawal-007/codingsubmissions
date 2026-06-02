class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if (i + 1) % 3 != 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna