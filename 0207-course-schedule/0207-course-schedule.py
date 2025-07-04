from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        adjList = defaultdict(list)
        # adjList
        for crs, nei in prerequisites:
            adjList[crs].append(nei)

        processing = set()
        visited = set()

        # dfs
        def dfs(crs):
            
            # if crs in processing --> cycle false
            if crs in processing:
                return False
            # if crs in visited --> already processing true
            if crs in visited:
                return True

            # add crs to processing
            processing.add(crs)

            # traverse neighbors if any neighbor returns True 
            # if any neighbor returns False --> cycle so return False
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            
            # remove from processing
            processing.remove(crs)

            # add to visited
            visited.add(crs)
            return True

        # traverse courses --> if one course has a cycle return False
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True