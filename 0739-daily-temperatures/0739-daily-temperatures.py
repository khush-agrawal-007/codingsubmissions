class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stk = []
        ans = [0]*len(temp)

        for i,t in enumerate(temp):
            while stk and stk[-1][0] <t:
                stk_t,stk_i = stk.pop()
                ans[stk_i] = i - stk_i

            stk.append((t,i))
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna