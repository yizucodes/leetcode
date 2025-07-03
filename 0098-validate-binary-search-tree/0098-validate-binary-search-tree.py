# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # one node --> true

        def dfs(node, mini, maxi):
            if not node:
                return True
            
            # check for valid boundary
            if node.val < mini or node.val > maxi:
                return False
            
            # update boundaries and call dfs
            left = dfs(node.left, mini, node.val)
            right = dfs(node.right, node.val, maxi)
            
            return left and right

        return dfs(root, float('-inf'), float('inf'))
        