"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # empty graph return
        if not node:
            return

        visited = {}

        
# Better logic:
# 1. Check if already cloned
# 2. If not, create clone and store mapping
# 3. Process neighbors and connect them



        def dfs(original):
         
            if original not in visited:
                cloned = Node(original.val)
                # update mapping
                visited[original] = cloned
                for nei in original.neighbors:
                    cloned_neighbor = dfs(nei)
                    cloned.neighbors.append(cloned_neighbor)

            else:
                return visited[original]

            return cloned
        
        return dfs(node)
