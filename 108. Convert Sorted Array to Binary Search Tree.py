from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive_search(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = recursive_search(left, middle - 1)
            root.right = recursive_search(middle + 1, right)
            return root
        return recursive_search(0, len(nums) - 1)
