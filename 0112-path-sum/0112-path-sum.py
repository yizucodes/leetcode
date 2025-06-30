# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # empty root return false
        if not root:
            return False

        # dfs on path to find the sum
        def dfs(node, remSum):
            # base case
            if not node:
                return False

            remSum -= node.val

            # you are at leaf node (right and left node are None)
            # check if remainingSum == 0 --> return True or False

            if not node.left and not node.right:
                return remSum == 0

    

            # go left and right subtree
            leftTree = dfs(node.left, remSum)
            rightTree = dfs(node.right, remSum)

            return leftTree or rightTree

        return dfs(root, targetSum)