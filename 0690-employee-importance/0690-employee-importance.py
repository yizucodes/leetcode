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

        empMap = {}

        # build employee map
        # id : Employee object (not just importance!)
        for emp in employees:
            empMap[emp.id] = emp

        # recursively find the sum:
        # - get employee by id
        # - add their importance
        # - recursively sum all subordinates

    
        def dfs(empId):
            total = 0
            importance = empMap[empId].importance
            subordinates =  empMap[empId].subordinates

            # add importance
            total += importance

            # sum subordinates
            for subId in subordinates:
                total += dfs(subId)
                

            return total


        return dfs(id)

