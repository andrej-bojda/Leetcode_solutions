from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        biggest_area = 0
        while i < j :
            curr_area = (j - i) * min(heights[j], heights[i])
            if curr_area > biggest_area:
                biggest_area = curr_area
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return biggest_area




if __name__ == "__main__":
    solver = Solution()
    print(solver.maxArea(heights=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]))