class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for op in operations:
            if op == '+':
                stk.append(stk[-1]+stk[-2])
            elif op == 'D':
                stk.append(stk[-1]*2)
            elif op == 'C':
                stk.pop()
            else:
                stk.append(int(op))

        return sum(stk)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna