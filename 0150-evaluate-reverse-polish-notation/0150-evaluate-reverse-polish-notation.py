class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                b,a = stk.pop(),stk.pop() # so that right side will be most recent and left side will be us se chota wala value
                if t == '+':
                    stk.append(int(a+b))
                elif t =='*':
                    stk.append(int(a*b))
                elif t =='/':
                    stk.append(int(a/b))
                else :
                    stk.append(int(a-b))
            else:
                stk.append(int(t))
        return stk[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna