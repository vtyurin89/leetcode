from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return nums1
        else:
            m, n = m - 1, n - 1
            main_pointer = len(nums1) - 1
            while m >= 0 and n >= 0:
                if nums1[m] > nums2[n]:
                    temp = nums1[m]
                    nums1[main_pointer] = nums1[m]
                    nums1[m] = temp
                    m -= 1
                elif nums1[m] <= nums2[n]:
                    nums1[main_pointer] = nums2[n]
                    n -= 1
                main_pointer -= 1
            if n >= 0:
                while n >= 0:
                    nums1[main_pointer] = nums2[n]
                    main_pointer -= 1
                    n -= 1


solution = Solution()

nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
m, n = 3, 3
solution.merge(nums1, m, nums2, n)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1, nums2 = [1], []
m, n = 1, 0
solution.merge(nums1, m, nums2, n)
assert nums1 == [1]

nums1, nums2 = [0], [1]
m, n = 0, 1
solution.merge(nums1, m, nums2, n)
assert nums1 == [1]