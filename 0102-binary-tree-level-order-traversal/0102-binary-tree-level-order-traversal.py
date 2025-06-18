# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        res = []
      
        

        while queue:
            levels = len(queue)
            curr_level = []
            # Process entire current level
            for i in range(levels):
                # Pop and process ONE node
                popped = queue.pop(0)
                # Add its VALUE to curr_level
                curr_level.append(popped.val)

                # Add its CHILDREN to queue
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            
                # After processing ALL nodes in level:
                # Add curr_level to res
            res.append(curr_level)

        return res