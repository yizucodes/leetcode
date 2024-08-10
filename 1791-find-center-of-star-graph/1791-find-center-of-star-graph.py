class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Find edge with at lease two edges

        v1 = edges[0][0]
        v2 = edges[0][1]

        if v1 in edges[1]:
            return v1
        
        return v2
    