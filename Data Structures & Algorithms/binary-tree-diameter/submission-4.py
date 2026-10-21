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

        def depth(root):
            if not root:
                return 0

            nonlocal diameter
            leftSide = root.left
            rightSide = root.right

            leftDepth = depth(root.left)
            rightDepth = depth(root.right)

            diameter = max(diameter, leftDepth + rightDepth)


            return 1 + max(leftDepth, rightDepth)
        depth(root)
        return diameter
        


        