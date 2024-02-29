class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        for i in range(33):
            if 2**i == n:
                return True
        return False

solution = Solution()
assert solution.isPowerOfTwo(1) is True
assert solution.isPowerOfTwo(16) is True
assert solution.isPowerOfTwo(3) is False
assert solution.isPowerOfTwo(-100) is False


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0


solution2 = Solution2()
assert solution2.isPowerOfTwo(1) is True
assert solution2.isPowerOfTwo(16) is True
assert solution2.isPowerOfTwo(3) is False
assert solution2.isPowerOfTwo(-100) is False
