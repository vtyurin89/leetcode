class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1



solution = Solution()
assert solution.isPowerOfThree(27) is True
assert solution.isPowerOfThree(0) is False
assert solution.isPowerOfThree(-1) is False
