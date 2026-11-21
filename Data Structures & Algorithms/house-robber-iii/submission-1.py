class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        memo = {}

        def dfs(node):
            if not node:
                return 0

            rob = node.val

            if node in memo:
                return memo[node]

            if node.left:
                rob += dfs(node.left.left) + dfs(node.left.right)

            if node.right:
                rob += dfs(node.right.left) + dfs(node.right.right)

            skip = dfs(node.left) + dfs(node.right)

            memo[node] = max(rob, skip)
            return memo[node]

        return dfs(root)