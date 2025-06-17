# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # one node return 1
        good = 0

        def dfs(curr, maxVal):
            
            # base case
            if curr is None:
                return 0

            nonlocal good
            # check if curr.val >= maxVal --> good += 1
            if curr.val >= maxVal:
                good += 1

            # adjust maxVal
            newMaxVal = max(curr.val, maxVal)

            dfs(curr.left, newMaxVal)
            dfs(curr.right, newMaxVal)

            return good

        return dfs(root, root.val)