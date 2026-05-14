class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and stack[-1]>c and k>0:
                k-=1
                stack.pop()
            stack.append(c)
        
        stack = stack[:len(stack)-k]
        res = ''.join(stack).lstrip('0')
        return res if res else '0'
        # logic : pop curr no. till next value is not greater , if greater and not eql then append else pop . then return what is left in stack and convert in int the str to avoid leading zeros 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna