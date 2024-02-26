from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        result, cursor = 0, len(citations)
        if cursor == 1 and citations[0] == 0:
            return 0

        citations.sort()

        for i in range(cursor):
            if citations[i] < cursor - i:
                result = citations[i]
            else:
                result = max(result, cursor - i)
        return result


solution = Solution()
assert solution.hIndex([3,0,6,1,5]) == 3
assert solution.hIndex([1,3,1]) == 1
