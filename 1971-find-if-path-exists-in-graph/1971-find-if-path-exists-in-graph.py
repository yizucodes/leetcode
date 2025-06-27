from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # if source or destination not in graph --> return False

        # adjacency list
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u) # bidirectional

        # dfs traversal
        visited = set()
        def dfs(node):

            # base case: reached destination
            if destination == node:
                return True

            # add to visited
            visited.add(node)

            # traverse neighbors
            for nei in adjList[node]:
                # traverse neighbors if not visited
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False

        return dfs(source)