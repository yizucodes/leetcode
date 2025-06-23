class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []              # Store the final course order
        visited = set()       # Courses completely processed (no cycles found)
        processing = set()    # Courses currently being processed (for cycle detection)

        def dfs(pr):
            # Check for cycle: if we're already processing this course in current path
            if pr in processing: 
                return False
                
            # If already completely processed, skip
            if pr in visited:
                return True
            
            # Start processing this course
            processing.add(pr)

            # Check all prerequisites of current course
            for nei in adjList[pr]:
                if not dfs(nei):        # If any prerequisite fails
                    return False       

            # Finished checking all prerequisites successfully
            processing.remove(pr)   # Remove from current path
            visited.add(pr)         # Mark as completely processed
            res.append(pr)          # Add to result (safe to take this course)
            return True           

        # Build adjacency list: course -> list of its prerequisites
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []         # Initialize empty prerequisite lists

        # Populate adjacency list from prerequisites
        for course, pr in prerequisites:
            adjList[course].append(pr)  # course requires prerequisite pr

        # Check each course for cycles
        for crs in range(numCourses):
            if crs not in visited:          # Only process unvisited courses
                if not dfs(crs):            # If cycle found
                    return []              

        return res