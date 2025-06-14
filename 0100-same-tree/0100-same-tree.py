# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both trees are empty
        if q is None and p is None:
            return True

        if p is None or q is None:
            return False
        # base case return false if one p.val != q.val
        if p.val != q.val:
            return False
        
        # traverse left subtree of p is sames as q
        # traverse right subtree of p is sames as q
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

