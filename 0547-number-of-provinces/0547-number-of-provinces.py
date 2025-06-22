class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        numP = 0
        visited = [0] * len(isConnected)

        # dfs on the other cities
        # check if other city is not visited
        # if other_city is 1 means it's connected so do dfs on that other city
        def dfs(ct):
            visited[ct] = 1
            for otherCt in range(len(isConnected[ct])):
                # visited before
                if isConnected[ct][otherCt] == 1 and visited[otherCt] == 0:
                    dfs(otherCt)
            
            return ct
    
        # traverse cities which is index in isConnected
        for city in range(len(isConnected)):
            # city has not been visited
            if visited[city] == 0:
                numP += 1
                dfs(city)

        return numP