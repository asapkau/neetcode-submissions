# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r, sr):
            if not r and not sr:
                return True
            if not r or not sr:
                return False
            
            if r.val != sr.val:
                return False

            
            
            return isSame(r.left, sr.left) and isSame(r.right, sr.right)

        def dfs(node):
            if not node:
                return False

            if isSame(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)