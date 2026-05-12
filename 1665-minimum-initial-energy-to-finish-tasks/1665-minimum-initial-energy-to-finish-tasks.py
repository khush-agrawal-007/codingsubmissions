class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort tasks by the difference (minimum - actual) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            # If we don't have enough energy to start the task, we must add to our initial pool
            if current_energy < minimum:
                initial_energy += (minimum - current_energy)
                current_energy = minimum
            
            # Consume the energy for the task
            current_energy -= actual
            
        return initial_energy

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna