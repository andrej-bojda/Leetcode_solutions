from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                length = 1
                while x + 1 in nums_set:
                    length += 1
                    x += 1
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    solver = Solution()
    print(solver.longestConsecutive(nums = [0,3,2,5,4,6,1,1]))