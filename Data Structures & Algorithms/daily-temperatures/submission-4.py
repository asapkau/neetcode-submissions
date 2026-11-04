class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                if temperatures[i] > temperatures[stack[-1]]:
                    oldIndex = stack.pop()
                    res[oldIndex] = i - oldIndex
            stack.append(i)
        return res

