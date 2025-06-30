# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # one node return [str(root.val)]

        # node -> node2

        res = []

        def dfs(node, path):

            if not node:
                return
            
            if not path:
                path = str(node.val)
            else:
                # Add current node to path
                path = path + '->' + str(node.val)
            
            # If leaf: add complete path to result
            if not node.left and not node.right:
                res.append(path)
            # If not leaf: recurse on children
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            return res
        
        return dfs(root, "")


