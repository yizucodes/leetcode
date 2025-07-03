# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr = root
        # if curr value is greater and p and q then go left
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # if curr value is less than p.val and q.val then go right
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            # else found lca
            else:
                return curr
     
        

        