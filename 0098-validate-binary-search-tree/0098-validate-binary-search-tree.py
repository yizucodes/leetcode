# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         FUNCTION isValidBST(root):
#     RETURN checkNode(root, -infinity, +infinity)

        # FUNCTION checkNode(node, min_allowed, max_allowed):
        def checkNode(node, mini, maxi):
                   #     IF node is null:
        #         RETURN true
            if not node:
                return True
 

                #     IF node.value <= min_allowed OR node.value >= max_allowed:
        #         RETURN false
            if node.val <= mini or node.val >= maxi:
                return False

            # left child, must be than current node
            leftValid = checkNode(node.left, mini, node.val)
            rightValid = checkNode(node.right, node.val, maxi)
            
            return leftValid and rightValid
        
        return checkNode(root, float('-inf'), float('inf'))

            
        #     // For left child: it must be less than current node
        #     // So update max_allowed to current node's value
        #     left_is_valid = checkNode(node.left, min_allowed, node.value)
            
        #     // For right child: it must be greater than current node
        #     // So update min_allowed to current node's value
        #     right_is_valid = checkNode(node.right, node.value, max_allowed)
            
        #     RETURN left_is_valid AND right_is_valid
