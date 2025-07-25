# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=-math.inf, upper=math.inf) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            
            return True
        
        return helper(root)