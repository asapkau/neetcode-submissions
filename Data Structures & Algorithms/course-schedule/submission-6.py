class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        completed = set()

        courses = {}

        for course, preReq in prerequisites:
            if preReq not in courses:
                courses[preReq] = []
            courses[preReq].append(course)
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in completed:
                return True
            
            visiting.add(course)

            for nextCourse in courses.get(course,[]):
                if not dfs(nextCourse):
                    return False
            
            visiting.remove(course)
            completed.add(course)
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True




        