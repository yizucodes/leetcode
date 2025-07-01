# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1 node then return 1
        
        # longest number of edge in entire tree
        maxD = 0

        def dfs(node):
            nonlocal maxD
            if not node:
                return 0
            
            # calculate left height
            left = dfs(node.left)
            right = dfs(node.right)
            
            currD = left + right

            # find max of height
            maxD = max(currD, maxD)
            
            # Do something with left and right
            return 1 + max(left, right)
        
        dfs(root)
        return maxD

