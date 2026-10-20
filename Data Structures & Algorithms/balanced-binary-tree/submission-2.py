# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        balanced = True

        def maxDepth(root):
            if not root:
                return 0

            nonlocal balanced
            leftHeight = maxDepth(root.left)
            rightHeight = maxDepth(root.right)
            difference = abs(leftHeight - rightHeight)
            
            if difference > 1:
                balanced = False

            return 1 + max(rightHeight, leftHeight)
        
        maxDepth(root)
        return balanced
        
                
            
        