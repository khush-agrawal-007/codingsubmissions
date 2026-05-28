from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Helper function to determine if a new index 'i' is better than 'current_best'
        def is_better(i: int, current_best: int) -> bool:
            if current_best == -1: 
                return True
            
            len_i = len(wordsContainer[i])
            len_curr = len(wordsContainer[current_best])
            
            # Prefer shorter length
            if len_i < len_curr: 
                return True
            # Tie-breaker: prefer smaller index
            if len_i == len_curr and i < current_best: 
                return True
                
            return False

        # Find the globally best index (handles queries that match no characters)
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if is_better(i, global_best_idx):
                global_best_idx = i
                
        root.best_idx = global_best_idx

        # Build the Trie
        for i, word in enumerate(wordsContainer):
            curr = root
            # Insert the word in reverse
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                # Update the best index for this prefix (suffix in original word)
                if is_better(i, curr.best_idx):
                    curr.best_idx = i

        # Process the queries
        ans = []
        for query in wordsQuery:
            curr = root
            # Search the query in reverse
            for char in reversed(query):
                if char not in curr.children:
                    break  # Stop at the longest match found
                curr = curr.children[char]
            
            ans.append(curr.best_idx)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna