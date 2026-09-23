class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        
        

        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax = [0] * len(height)
        rightMax[len(height) - 1] = height[len(height) - 1]

        for i in range(len(height) - 2 , -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        totalWater = 0

        for i in range(len(height)):
            waterAtI = min(leftMax[i], rightMax[i]) - height[i]
            totalWater += waterAtI
        return totalWater



        