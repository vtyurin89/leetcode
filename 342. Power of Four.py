class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursive_checkfour(num):
            if num % 4 != 0 or num == 1:
                return num
            return recursive_checkfour(num / 4)

        if n <= 0:
            return False
        return recursive_checkfour(n) == 1


solution = Solution()
assert solution.isPowerOfFour(16) is True
assert solution.isPowerOfFour(5) is False
assert solution.isPowerOfFour(1) is True
