from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left + 1, right + 1]
            elif summation > target:
                right -= 1
            else:
                left += 1
        return []

if __name__ == "__main__":
    solver = Solution()
    print(solver.twoSum(numbers = [1,2,3,4], target = 3))