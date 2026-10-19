class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftListPtr = 0
        rightListPtr = len(matrix) - 1

        while leftListPtr <= rightListPtr:
            midListPtr = (leftListPtr + rightListPtr) // 2

            if matrix[midListPtr][0] > target:
                rightListPtr = midListPtr - 1
            
            elif matrix[midListPtr][-1] < target:
                leftListPtr = midListPtr + 1
            elif matrix[midListPtr][0] <= target <= matrix[midListPtr][-1]:
                l = 0
                r = len(matrix[midListPtr]) - 1

                while l <= r:
                    mid = (l + r) // 2

                    if matrix[midListPtr][mid] < target:
                        l = mid + 1
                    elif matrix[midListPtr][mid] > target:
                        r = mid - 1
                    elif matrix[midListPtr][mid] == target:
                        return True
                return False
        
        return False


        