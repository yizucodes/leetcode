# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # one node --> True

        # duplicates child nodes for either side --> False
        def isValid(node, minVal, maxVal):
            if node is None:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False
            
            left = isValid(node.left, minVal, node.val)
            right = isValid(node.right, node.val, maxVal)

            return left and right

        
        return isValid(root, float('-inf'), float('inf'))


    

            
            

