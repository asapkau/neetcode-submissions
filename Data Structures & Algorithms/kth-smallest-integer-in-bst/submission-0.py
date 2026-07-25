# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #use inorder BST traversal, and then from the list return k-1 index

        if root is None:
            return 0
        
        self.count = 0
        self.answer = None

        

        def inorderTraversal(node):
            if node is None or self.answer is not None:
                return
            leftTraversal = inorderTraversal(node.left)

            self.count += 1

            if self.count == k:
                self.answer = node.val
                return 

        
            rightTraversal = inorderTraversal(node.right)
        inorderTraversal(root)
        return self.answer
        
        



            