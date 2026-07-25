# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def dfs(node, maxValue):
            if not node:
                return 0

            if node.val >= maxValue:
                good = 1
            else:
                good = 0
            
            newMax = max(node.val, maxValue)
                
                
            return good + dfs(node.left, newMax) + dfs(node.right, newMax)
        
        return dfs(root, root.val)    