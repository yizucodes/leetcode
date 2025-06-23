class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        visited = set()
        processing = set()

        def dfs(pr):

            # base case: if cycle return []
            if pr in processing: 
                return False
            if pr in visited:
                return True

            processing.add(pr)

            for nei in adjList[pr]:
                if not dfs(nei):
                    return False

            processing.remove(pr)
            visited.add(pr)
            res.append(pr)
            return True

        # create adjacency list
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []

        for course, pr in prerequisites:
            adjList[course].append(pr)

        # dfs on each course
        for crs in range(numCourses):
            if crs not in visited:
                if not dfs(crs): return []

        return res