# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        # Step 1 & 2: Create nodes and map relationships
        for parent_val, child_val, is_left in descriptions:
            # Create parent if it doesn't exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            
            # Create child if it doesn't exist
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Link child to parent
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Keep track of all children to find the root later
            children.add(child_val)
            
        # Step 3: Find the root (the only node not in the children set)
        for val in nodes:
            if val not in children:
                return nodes[val]
                
        return None

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna