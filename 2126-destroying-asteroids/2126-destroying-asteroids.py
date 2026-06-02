class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Step 1: Sort the asteroids from smallest to largest
        asteroids.sort()
        
        # Step 2: Try to destroy them one by one
        for asteroid in asteroids:
            if mass < asteroid:
                return False  # The planet is too small
            mass += asteroid  # The planet absorbs the asteroid
            
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna