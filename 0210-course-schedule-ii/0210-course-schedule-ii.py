from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build an adjacency list
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        processing = set()
        visited = set()
        res = []

        # dfs on the graph to find path
        def dfs(course):
            # base case: course is cycle
            if course in processing:
                return False
            # base case: course processed
            if course in visited:
                return True
            
            processing.add(course)

            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            
            processing.remove(course)
            visited.add(course)
            res.append(course)

            return True

        # visited
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res







