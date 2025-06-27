class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build adjacency list
        adjList = {}  # or use defaultdict(list)
        for course, prereq in prerequisites:
            # This means: to take 'course', I need to first take all courses in adjList[course]
            if course not in adjList:
                adjList[course] = []
            adjList[course].append(prereq)
            
        # Two separate tracking structures:
        visiting = set()  # Currently in the DFS path (gray nodes)
        visited = set()   # Completely done with DFS (black nodes)
    
        def dfs(crs):
            # If we're currently visiting this course, we found a cycle!
            if crs in visiting:
                return False
                
            # If we already completely processed this course, it's safe
            if crs in visited:
                return True
                
            # Mark as currently visiting
            visiting.add(crs)
            
            # Check if any prerequisite has a cycle
            if crs in adjList:
                for prereq in adjList[crs]:
                    if not dfs(prereq):
                        return False
                    
            # Done visiting this course - remove from visiting, add to visited
            visiting.remove(crs)
            visited.add(crs)
            
            return True
    
        # Check every course (some might not be connected)
        for course in range(numCourses):
            if not dfs(course):
                return False
                
        return True

