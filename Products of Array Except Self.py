from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = []

        curr = 1
        for num in nums:
            output.append(curr)
            curr *= num

        j = len(nums) - 1
        curr = 1
        while j >= 0:
            output[j] *= curr
            curr *= nums[j]
            j -= 1

        return output






