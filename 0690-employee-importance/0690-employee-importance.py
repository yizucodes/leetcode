"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        # map first employees { id: importance }
        empMap = {}

        for emp in employees:
            empMap[emp.id] = emp
        res = 0

        def dfs(targetId):

            nonlocal res
            # base case: id not in empMap return
            if targetId not in empMap:
                return

            # lookup employee in lookup table

            # sum its importance 
            res = res + empMap[targetId].importance

            # sum importance for each subordinates
            for subId in empMap[targetId].subordinates:
                dfs(subId)
            
        dfs(id)
        return res