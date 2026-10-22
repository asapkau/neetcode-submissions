# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        goodNode = 0

        def dfs(node, maxSeen):
            nonlocal goodNode
            if not node:
                return 0
            
            if node.val >= maxSeen:
                goodNode += 1
                
                
            newMax = max(maxSeen, node.val)
            

            dfs(node.left, newMax)
            dfs(node.right, newMax)
        dfs(root, root.val)
        return goodNode
        