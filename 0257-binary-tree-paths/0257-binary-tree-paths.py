# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        # def dfs(node, path):
        def dfs(node, path):

            # base case
            # reached leaf node
            # append the path to res
            if not node:
                return ""

             # concatenate node.val to path string
            nodeVal = str(node.val)
        
            if path == "":
                path += nodeVal
            else:
                path = path + '->' + nodeVal

            if not node.left and not node.right:
                res.append(path)

            # call dfs on update path string on left and right subtree
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res