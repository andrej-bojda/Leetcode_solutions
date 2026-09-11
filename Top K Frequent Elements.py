from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        sorted_list = sorted(count.keys(), key=lambda num: count[num], reverse=True)
        return sorted_list[:k]

if __name__ == "__main__":
    solver = Solution()
    print()