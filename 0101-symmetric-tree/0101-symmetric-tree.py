# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(s, t):
            # Handle case where both nodes are None
            if s is None and t is None:
                return True
            
            # Handle case where only one node is None
            if s is None or t is None:
                return False
            
            # Check if the current node values match
            if s.val != t.val:
                return False
            
            # Recursively check if left subtree of s mirrors right subtree of t
            if not isMirror(s.left, t.right):
                return False
            
            # Recursively check if right subtree of s mirrors left subtree of t
            if not isMirror(s.right, t.left):
                return False
            
            # If all checks passed, trees are mirrors)
            return True

        
        return isMirror(root.left, root.right)



