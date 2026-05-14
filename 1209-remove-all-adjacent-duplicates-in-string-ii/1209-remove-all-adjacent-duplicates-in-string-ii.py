class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] +=1
            else:
                stack.append([c,1])
            if stack[-1][1] == k:
                stack.pop()

        result = ""
        for char , count in stack:
            result += (char*count)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna