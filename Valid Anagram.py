class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check_s = {}
        check_t = {}
        for i in range(len(s)):
            if s[i] in check_s:
                check_s[s[i]] += 1
            else:
                check_s[s[i]] = 1
            if t[i] in check_t:
                check_t[t[i]] += 1
            else:
                check_t[t[i]] = 1
        return check_s == check_t

if __name__ == "__main__":
    solver = Solution()
    print(solver.isAnagram(s = "anagram", t = "nagaram"))
    print(solver.isAnagram(s = "rat", t = "car"))