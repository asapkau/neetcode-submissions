class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
            
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    prevIndex = stack.pop()
                    result[prevIndex] = i - prevIndex
                stack.append(i)
                continue
        return result
                
        