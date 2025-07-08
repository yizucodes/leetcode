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
        if not node:
            return None
            
        visited = {} # original with cloned   

        # iterate through adjList
        def dfs(original):
            if not original:
                return
            
            # if cloned already --> return cloned version
            if original in visited:
                return visited[original]

            # clone first node
            cloned = Node(original.val)

            # mark as visited
            visited[original] = cloned

            # clone each of the nodes neigh nodes 
            # append cloned nei to list
            if original.neighbors:
                for nei in original.neighbors:
                    clonedNei = dfs(nei)
                    cloned.neighbors.append(clonedNei)
                    
            return cloned



        res = dfs(node)

        return res