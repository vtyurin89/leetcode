from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        nodes = deque([root])
        while nodes:
            current_sum = 0
            num_nodes = len(nodes)
            for i in range(num_nodes):
                node = nodes.pop()
                current_sum += node.val
                if node.left:
                    nodes.appendleft(node.left)
                if node.right:
                    nodes.appendleft(node.right)
            result.append(current_sum / num_nodes)
        return result



