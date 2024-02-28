from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def generate_linked_list(lst: List[int]) -> ListNode:
        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    @staticmethod
    def linked_list_to_list(head: ListNode) -> List[int]:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head.next is None:
            return head
        dummy = ListNode(val=0, next=head)

        current, prev = head, dummy
        for i in range(left - 1):
            prev = current
            current = current.next

        left_prev = prev
        rev_end = current
        prev = None

        for i in range(right - left + 1):
            middleman = current.next
            current.next = prev
            prev = current
            current = middleman
        left_prev.next = prev
        rev_end.next = current

        return dummy.next



solution = Solution()
head1 = solution.generate_linked_list([1,2,3,4,5])
solution1 = solution.reverseBetween(head1, 2, 4)
assert solution.linked_list_to_list(solution1) == [1, 4, 3, 2, 5]
head2 = solution.generate_linked_list([5])
solution2 = solution.reverseBetween(head2, 1, 1)
assert solution.linked_list_to_list(solution2) == [5]
head3 = solution.generate_linked_list([4,0,-1,3])
solution3 = solution.reverseBetween(head3, 1, 4)
assert solution.linked_list_to_list(solution3) == [3,-1,0,4]