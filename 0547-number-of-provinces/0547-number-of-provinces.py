class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # if one item then 1 province
        numP = 0
        visited = set()

        # dfs
        def dfs(city):
            # base case: visited city
            if city in visited:
                return []
            
            # mark city as visited
            visited.add(city)

            # check for connected cities
            # if connected, do dfs on that connected city
            for other in range(len(isConnected)):
                if isConnected[city][other] == 1:
                    if other not in visited:
                        dfs(other)

        # traverse every component with dfs
        for city in range(len(isConnected)):
            if city not in visited:
                numP += 1
                dfs(city)
            
        return numP

