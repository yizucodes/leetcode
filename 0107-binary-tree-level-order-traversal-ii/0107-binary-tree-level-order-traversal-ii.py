
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # root in the queue
        q = [root]

        res = []

        # while queue is not empty
        while q:
            levels = len(q)
            currLevel = []

            # process each levels
            for i in range(levels):
                popped = q.pop(0)
                # add next level nodes to q
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

                # store current level to res
                currLevel.append(popped.val)
            res.append(currLevel)

        return res[::-1]