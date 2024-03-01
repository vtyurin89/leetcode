from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def check_sum(node, sum):
            if not node:
                return False
            current_sum = node.val + sum
            if current_sum == targetSum and not node.left and not node.right:
                return True
            return check_sum(node.left, current_sum) or check_sum(node.right, current_sum)
        return check_sum(root, sum)
