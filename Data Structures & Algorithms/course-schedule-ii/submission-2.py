class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        completed = set()
        res = []

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

            visiting.remove(course)
            completed.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res[::-1]
        
        