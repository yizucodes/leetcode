class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if no prereqs then return True
        if not prerequisites:
            return True

        visited = set()
        def dfs(pr):

            # base case if there if couse is visited
            if pr in visited:
                return False
            
            if adjList[pr] == []:
                return True

            # add to visited set
            visited.add(pr)

            # Checks if path to complete prereq course can be completed
            for pre in adjList[pr]
                if not dfs(pre): return False


            # remove from set after checking
            visited.remove(pr)
            
            # assign value to [] as it's being visited
            adjList[pr] = []
            return True

        # Build adjacency list first - {course: [list of prerequisites]}
        adjList = {}

        # Initialize empty lists for all courses
        for i in range(numCourses):
            adjList[i] = []

        # Add prerequisites 
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True


