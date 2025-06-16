# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # empty or 1 node --> true
        
        # dfs
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # left tree imbalanced
            if left == -1:
                return -1

            # right tree imbalanced
            if right == -1:
                return -1
            
            hDiff = abs(left - right)

            # check if balanced
            if hDiff > 1:
                return -1
            
            # returning height
            return max(left, right) + 1

        return dfs(root) != -1
            












        