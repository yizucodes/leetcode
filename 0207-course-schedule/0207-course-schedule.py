from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # build adjList courses --> prerequisites
        adjList = defaultdict(list)

        for crs, pr in prerequisites:
            adjList[crs].append(pr)

        visited = set()
        processing = set()

        def dfs(crs):
            
            # cycle
            if crs in processing:
                return False
            
            # already visited
            if crs in visited:
                return True

            # processing
            processing.add(crs)

            # dfs on each prereq
            for prereq in adjList[crs]:
                if not dfs(prereq):
                    return False
            
            processing.remove(crs)
            visited.add(crs)

            return True


        # traverse courses
        for crs in range(numCourses): 
            if not dfs(crs):
                return False

        
        return True