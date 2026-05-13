class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a<0 and stack[-1] >0:
                diff = a + stack[-1]

                if diff<0:
                    stack.pop()
                elif diff>0:
                    a=0
                else:
                    a = 0
                    stack.pop()
            
            if a:
                stack.append(a)
        return stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna