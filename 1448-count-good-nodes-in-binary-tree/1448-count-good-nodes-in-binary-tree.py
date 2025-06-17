# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # current
        good = 0
       
        def dfs(curr, maxVal):
            nonlocal good

            if curr is None:
                return 0
            
            # check if curr.val > max --> good + 1
            if curr.val >= maxVal:
                good += 1
            
            newMaxVal = max(curr.val, maxVal)

            left = dfs(curr.left, newMaxVal)
            right = dfs(curr.right, newMaxVal)
            
            return good

        return dfs(root, root.val)