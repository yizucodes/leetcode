# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.count = 0
        self.res = None
        
        def dfs(node):
            # if node not found or found a result then stop dfs
            if not node or self.res:
                return
            
            dfs(node.left)
            self.count += 1
            if k == self.count:
                self.res = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.res
        
       