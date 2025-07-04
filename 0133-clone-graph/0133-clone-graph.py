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
        # empty graph
        if not node:
            return None

        # 1 node

        # nodeMap { original: cloned }
        nodeMap = {} 
        
            # dfs
        def dfs(original):
        # base case: visited already
            if original in nodeMap:
                return nodeMap[original]

            # clone original node
            cloned = Node(original.val)

            # mark as visited
            nodeMap[original] = cloned

            # clone neighbors each
            # attach neighbors to cloned node
            for nei in original.neighbors:
                clonedNei = dfs(nei)
                cloned.neighbors.append(clonedNei)
               
            return cloned

        return dfs(node)