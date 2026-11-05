# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        def dfs(root ,minn, maxx):
            if not root:
                return True

            if root.val <= minn or root.val >= maxx:
                return False
            
            isLeftValid = dfs(root.left, minn, root.val)
            isRightValid = dfs(root.right, root.val, maxx)
        
            return isLeftValid and isRightValid
        return dfs(root, float("-inf"), float("inf"))
            

        