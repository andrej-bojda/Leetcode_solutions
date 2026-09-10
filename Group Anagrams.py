from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_dict = dict()
        for word in strs:
            key = "".join(sorted(word))
            if key not in check_dict:
                check_dict[key] = []
            check_dict[key].append(word)
        return list(check_dict.values())

if __name__ == "__main__":
    solver = Solution()
    print(solver.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))