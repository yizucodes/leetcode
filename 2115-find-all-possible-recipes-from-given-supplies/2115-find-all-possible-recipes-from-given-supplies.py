from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # no supplies --> return []
        res = []

        # adjList
        # recipe: [ingredients]
        adjList = defaultdict(list)
        for i in range(len(recipes)):
            adjList[recipes[i]] = ingredients[i]

        processing = set()
        visited = set()

        def dfs(item):  # Could be a recipe OR an ingredient
            # Base cases:
            # 1. If item in supplies → return True (we have it!)
            if item in supplies:
                return True
            # 2. If item in processing → return False (cycle!)
            if item in processing:
                return False

            # 3. If item in visited → return what we determined before
            if item in visited: # check
                return True
            
            # If item is not a recipe → return False (can't make it)
            if item not in recipes:
                return False  
            
            # If item IS a recipe:
            # - Add to processing
            processing.add(item)
            # - Check ALL ingredients (DFS each one)
            for ing in adjList[item]:
            # - If any ingredient returns False → return False
                if not dfs(ing):
                    processing.remove(ing)
                    return False
            # - Remove from processing, add to visited
            processing.remove(item)
            visited.add(item)

            return True


            
        # traverse for each recipe
        for rec in recipes:
            if dfs(rec):
                res.append(rec)

        return res