# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter = 0
        def maxDepth(root):
            if not root:
                return 0
            
            nonlocal diameter

            leftHeight = maxDepth(root.left)
            rightHeight = maxDepth(root.right)
            diameter = max(diameter, leftHeight + rightHeight)
            
            return 1 + max(leftHeight, rightHeight)
        maxDepth(root)
        return diameter
        
        


        