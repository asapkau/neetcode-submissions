class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights) - 1
        maxArea = 0
        

        while l < h:
            base = h - l
            length = min(heights[l], heights[h])
            area = length * base
            maxArea = max(area, maxArea)

            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
                
        return maxArea


        