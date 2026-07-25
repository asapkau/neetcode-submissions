# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return 0
        #case 1: is p and q are both lesser than the root
        #case 2: if p and q are both more than the root
        #case 3: if p is less and q is more than root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


        else:
            return root

        