class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        res = []
        
        visiting = set()
        completed = set()

        def dfs(course):
            if course in completed:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            completed.add(course)
            res.append(course)
            return True

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            

        return res[::-1]
        
        