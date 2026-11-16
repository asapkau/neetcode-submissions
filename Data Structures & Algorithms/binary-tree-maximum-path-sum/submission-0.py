# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxValue = float("-inf")
        
        
        def dfs(root):
            if not root:
                return 0

            nonlocal maxValue

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            maxValue = max(root.val + left + right, maxValue)
            return root.val + max(left, right)

        dfs(root)
        return maxValue
        
        