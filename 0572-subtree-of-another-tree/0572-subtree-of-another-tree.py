# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # same trees return True
        def isIdentical(s, t):
            # both trees empty
            if s is None and t is None:
                return True
            
            # one tree empty
            if s is None or t is None:
                return False
            
            if s.val != t.val:
                return False

            return (isIdentical(s.left, t.left) and isIdentical(s.right, t.right))

        # check subRoot when you see a root that equals to root
        if root is None or subRoot is None:
            return False

        if root.val == subRoot.val:
            return isIdentical(root, subRoot)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



