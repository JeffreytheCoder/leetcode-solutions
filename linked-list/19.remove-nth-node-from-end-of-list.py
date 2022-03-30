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

# linked list, dummy head, fast and slow pointers [2/5]

# key: to remove the target node, stop pointer at its previous node, change link to target node's next
#   removeNthFromEnd(1, [1]) removes 1th node, so use dummy head to operate remove

# set fast and slow to dummy, fast move n steps first
# fast and slow move until fast reaches last node (not until None because slow gets to last (n+1)th node to remove last nth node)

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
    
# time: O(n)
# space: O(1)

# @lc code=end
