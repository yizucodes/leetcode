# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # dfs
        def dfs(node):
            nonlocal diameter
            if node is None:
                return 0
                
            # calculate depth for each side of tree
            left = dfs(node.left)
            right = dfs(node.right)

            # calc max
            diameter = max(left + right, diameter)

            # returns height of tree to be used by parent node to calculate diameter
            return max(left, right) + 1

        diameter = 0
        dfs(root)

        return diameter
        