from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build adjacency list
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS from root (node 1) to find maximum depth
        depth = [-1] * (n + 1)
        depth[1] = 0
        queue = deque([1])
        max_depth = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if depth[neighbor] == -1:  # unvisited
                    depth[neighbor] = depth[node] + 1
                    max_depth = max(max_depth, depth[neighbor])
                    queue.append(neighbor)
        
        # 2^(max_depth - 1) mod MOD
        return pow(2, max_depth - 1, MOD)