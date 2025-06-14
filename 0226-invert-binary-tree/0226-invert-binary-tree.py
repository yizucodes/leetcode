# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # empty tree base case
        if not root:
            return

        # assign left node to right node and vice versa
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
       
        return root