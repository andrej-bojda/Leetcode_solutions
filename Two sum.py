from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in values:
                return [values[complement], i]
            values[nums[i]] = i
        return []

if __name__ == "__main__":
    solver = Solution()
    print(solver.twoSum(nums=[2, 7, 11, 15], target=9))