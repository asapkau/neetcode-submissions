# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        counter = 0
        
        leftRoot = root.left
        rightRoot = root.right
        counter += 1

        leftDepth = self.maxDepth(leftRoot)
        rightDepth = self.maxDepth(rightRoot)

        return 1 + max(leftDepth, rightDepth)

        