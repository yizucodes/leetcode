class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """

        Start DFS from node 0 with current path [0]
        Base case: If current node is n-1, add a copy of current path to results
        For each neighbor of current node:

        Add neighbor to current path
        Recursively call DFS on neighbor
        Remove neighbor from current path (backtrack)


        Return all collected paths

        """
        
        res = []
        currPath = []

        # Start DFS from node with current path [0]

        def dfs(node):

            # Base case: if current node is n - 1, add to current path of res
            if node == (len(graph) - 1):
                res.append([0] + currPath)
            
            for neighbor in graph[node]:
                currPath.append(neighbor)
                dfs(neighbor)
                currPath.pop()

        dfs(0)
        return res

