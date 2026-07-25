# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            x = 0
            x = root.right
            root.right = root.left
            root.left = x

            invertLeftTree = self.invertTree(root.left)
            invertRightTree = self.invertTree(root.right)

            
        return root
        