#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# techniques: dummy head, fast and slow pointers


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        tmp = slow.next.next
        slow.next = tmp

        return dummy.next

# @lc code=end
