class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        completed = set()

        courses = {}

        for course, prereq in prerequisites:
            if prereq not in courses:
                courses[prereq] = []
            courses[prereq].append(course)

        def dfs(course):
            if course in visiting:
                return False
            
            if course in completed:
                return True
            
            visiting.add(course)

            for neighbor in courses.get(course, []):
                if not dfs(neighbor):
                    return False
                dfs(neighbor)
            visiting.remove(course)
            completed.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True