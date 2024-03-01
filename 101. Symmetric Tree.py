from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(left, right):
            if not left and not right:
                return True
            elif not left or not right or left.val != right.val:
                return False
            return check_symmetry(left.right, right.left) and check_symmetry(left.left, right.right)
        return check_symmetry(root.left, root.right)

