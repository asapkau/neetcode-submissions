class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights) - 1
        maxVol = 0

        while l < h:
            maxVol = max(maxVol, min(heights[l], heights[h]) * (h-l))

            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
        return maxVol
            