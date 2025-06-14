# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # helper isMirror
        def isMirror(left, right):

            # if left and right are both none return True
            if left is None and right is None:
                return True

            # if left OR right one of them is None return False
            if left is None or right is None:
                return False

            # if left value is not same as right value return False
            if left.val != right.val:
                return False

            # recurse for left and right AND right and left nodes
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)