class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        visiting = set()
        completed = set()


        def dfs(course):
            if course in visiting:
                return False
            
            if course in completed:
                return True

            visiting.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            completed.add(course)
            return True  
            

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


        