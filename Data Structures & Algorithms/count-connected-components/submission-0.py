class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # {
        #     0:[1]
        #     1:[0,2]
        #     2:[1]
        #     3:[4]
        #     4:[3]
        # }

        mapp = {}
        component = 0
        visited = set()

        for node, nextNode in edges:
            if node not in mapp:
                mapp[node] = []

            if nextNode not in mapp:
                mapp[nextNode] = []

            mapp[node].append(nextNode)
            mapp[nextNode].append(node)
        
        def dfs(node):
            visited.add(node)

            for neighbour in mapp.get(node, []):
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                component += 1
                dfs(node)
        return component

