from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0:
            return False

        left, right = 0, k

        if right not in range(len(nums)):
            right = len(nums) - 1

        nums_set = set()
        for letter in nums[left: right + 1]:
            if letter in nums_set:
                return True
            nums_set.add(letter)

        while right < len(nums) - 1:
            nums_set.remove(nums[left])
            left += 1
            right += 1
            if nums[right] in nums_set:
                return True
            nums_set.add(nums[right])
        return False


solution = Solution()
assert solution.containsNearbyDuplicate([1,2,3,1], 3) is True
assert solution.containsNearbyDuplicate([1,0,1,1], 1) is True
assert solution.containsNearbyDuplicate([1,2,3,1,2,3], 2) is False
assert solution.containsNearbyDuplicate([99,99], 2) is True
assert solution.containsNearbyDuplicate([1,2,1], 0) is False
assert solution.containsNearbyDuplicate([0,1,2,3,2,5], 3) is True

