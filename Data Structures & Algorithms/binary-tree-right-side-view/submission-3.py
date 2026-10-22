# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        levels = []
        q = deque([root])

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            levels.append(level)
        
        # print(levels)

        for level in levels:
            res.append(level[-1])
        
        return res


        # res = []
        # def dfs(node, depth):

        #     if not node:
        #         return None
            
        #     if depth == len(res):
        #         res.append(node.val)
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)

        
        # dfs(root, 0)
        # return res