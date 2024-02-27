class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for index in range(len(s)):
            if s[index] not in s_dict:
                s_dict[s[index]] = t[index]
            if t[index] not in t_dict:
                t_dict[t[index]] = s[index]
            if s_dict[s[index]] != t[index] or t_dict[t[index]] != s[index]:
                return False
        return True


solution = Solution()
assert solution.isIsomorphic("egg", "add") is True
assert solution.isIsomorphic("foo", "bar") is False
assert solution.isIsomorphic("paper", "title") is True
assert solution.isIsomorphic("badc", "baba") is False
