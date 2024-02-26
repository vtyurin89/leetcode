class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        pattern_dict = dict()
        pattern_set = set(s_list)
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = s_list[i]
            elif s_list[i] != pattern_dict.get(pattern[i]):
                return False
        if len(pattern_set) != len(pattern_dict):
            return False
        return True


solution = Solution()
assert solution.wordPattern("abba", "dog cat cat dog") is True
assert solution.wordPattern("abba", "dog cat cat fish") is False
assert solution.wordPattern("aaaa", "dog cat cat dog") is False
