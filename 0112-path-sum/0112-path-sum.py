# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # empty input is false
        if not root:
            return False

        # def dfs(node, remSum):
        def dfs(node, remSum):
            
            if not node:
                return False

            # update sum
            remSum = remSum - node.val

            # base 
            # reach to leaf
            if node.left == None and node.right == None:
                return remSum == 0

            # call dfs on left and rightsubtree
            left = dfs(node.left, remSum)
            right = dfs(node.right, remSum)

            # return true if either left or right is true
            return left or right

        
        return dfs(root, targetSum)


        