from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_list = set()
        for num in nums:
            if num in check_list:
                return True
            check_list.add(num)
        return False
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False