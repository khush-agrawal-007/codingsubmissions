import collections
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        LOG = 18 # 2^18 > 10^5
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # BFS to populate immediate parents and depth
        queue = collections.deque([(1, 0, 0)]) # (node, parent, depth)
        while queue:
            node, parent, d = queue.popleft()
            depth[node] = d
            up[0][node] = parent
            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node, d + 1))
                    
        # Populate Binary Lifting table
        for i in range(1, LOG):
            for j in range(1, n + 1):
                up[i][j] = up[i-1][up[i-1][j]]
                
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Level out the depths
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
                    
            if u == v:
                return u
                
            # Jump upwards together to find the LCA
            for i in range(LOG - 1, -1, -1):
                if up[i][u] != up[i][v]:
                    u = up[i][u]
                    v = up[i][v]
                    
            return up[0][u]
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[lca]
                # Fast modular exponentiation built into Python's pow()
                ans.append(pow(2, dist - 1, MOD))
                
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna