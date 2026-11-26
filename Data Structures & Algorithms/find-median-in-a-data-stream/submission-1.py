class MedianFinder:

    def __init__(self):
        self.nums = []  # Use a list to store all numbers

    def addNum(self, num: int) -> None:
        self.nums.append(num)  # Add each incoming number to the list

    def findMedian(self) -> float:
        self.nums.sort()  # Sort the list to find the middle value

        n = len(self.nums)  # Get total number of elements
        mid = n // 2  # Find the middle index

        if n % 2 == 1:  # If odd, there is one middle element
            return float(self.nums[mid])

        # If even, take the average of the two middle elements
        return (self.nums[mid - 1] + self.nums[mid]) / 2