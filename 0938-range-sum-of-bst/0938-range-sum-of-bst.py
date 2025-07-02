# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # one node and not betwee nlow and high --> return 0
        res = 0
        # dfs add to res if node.val is between low and high
        def dfs(node, low, high):
            nonlocal res
            # base case leaf
            if not node:
                return

            # if reach left value which is equal or less than low, stop traversal
            # if node.val <= low:
            #     return

            # if reach right subtree where value is equal or greater than high, stop traversal
            # if node.val >= high:
            #     return
            if low <= node.val <= high:
                res += node.val

            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, low, high)
        return res
