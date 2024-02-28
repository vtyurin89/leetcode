from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def generate_linked_list(lst: List[int]) -> ListNode | None:
        if len(lst) == 0:
            return None

        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            middleman = current.next
            current.next = prev
            prev = current
            current = middleman
        return prev


solution = Solution()
head1 = solution.generate_linked_list([1,2,3,4,5])
assert solution.reverseList(head1).val == 5
head2 = solution.generate_linked_list([1,2])
assert solution.reverseList(head2).val == 2
head3 = solution.generate_linked_list([])
assert solution.reverseList(head3) is None
