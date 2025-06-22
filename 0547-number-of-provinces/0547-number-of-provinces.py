class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        numP = 0

        # if not visited start province
        def dfs(city):

            "Mark the current city as visited so I remember I've been here"
            visited.add(city)

            "Start looking at every single city that exists in the whole map"
            for other in range(len(isConnected)):
                # Is there a direct road between my current city and this other city?
                if isConnected[city][other] == 1:
                    "If I found a connection, then check if I've already visited that connected city before"
                    if other not in visited:
                        dfs(other)
                    "If there's a connection AND I haven't been there yet, then go visit that city and repeat this whole process from there"

        # loop through cities
        for city in range(len(isConnected)):
            if city not in visited:
                numP += 1
                dfs(city)

       


        # count provinces
        return numP